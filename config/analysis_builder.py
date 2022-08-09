#!/usr/bin/env python3

def header_tmpl(filename: str):
    return """// -*- C++ -*-
//
/** FCCAnalysis module: @@@ANALYSIS_NAME@@@
 *
 * \\file """ + filename + """
 * \\author @@@AUTHOR_NAME@@@ <@@@AUTHOR_EMAIL@@@>
 *
 * Description:
 *   [...]
 */
"""

source_tmpl = header_tmpl('@@@SCRIPT_NAME@@@.cc') + """
#include "@@@ANALYSIS_NAME@@@/include/@@@SCRIPT_NAME@@@.h"
#include <iostream>

using namespace std;

namespace @@@ANALYSIS_NAME@@@ {
  void dummy_analysis() { cout << "Dummy analysis initialised." << endl; }

  rv::RVec<float> dummy_collection(const rv::RVec<edm4hep::ReconstructedParticleData>& parts) {
    rv::RVec<float> output;
    for (size_t i = 0; i < parts.size(); ++i)
      output.emplace_back(parts.at(i).momentum.x);
    return output;
  }
}  // namespace @@@ANALYSIS_NAME@@@"""

header_tmpl = header_tmpl('@@@SCRIPT_NAME@@@.h') + """
#ifndef @@@ANALYSIS_NAME@@@_@@@SCRIPT_NAME@@@_h
#define @@@ANALYSIS_NAME@@@_@@@SCRIPT_NAME@@@_h

#include "ROOT/RVec.hxx"
#include "edm4hep/ReconstructedParticle.h"

namespace @@@ANALYSIS_NAME@@@ {
  namespace rv = ROOT::VecOps;

  void dummy_analysis();
  rv::RVec<float> dummy_collection(const rv::RVec<edm4hep::ReconstructedParticleData>&);
}  // namespace @@@ANALYSIS_NAME@@@

#endif"""

class_tmpl = """namespace @@@ANALYSIS_NAME@@@ {
  struct dictionary {};
} // namespace @@@ANALYSIS_NAME@@@"""

xml_tmpl = """<lcgdict>
  <class name="@@@ANALYSIS_NAME@@@::dictionary"/>
</lcgdict>"""

def find_author():
    from subprocess import getoutput
    return (getoutput('git config --global --get user.name'),
            getoutput('git config --global --get user.email'))

def replace_all(input: str, repl) -> str:
    output = input
    for a, b in repl.items():
        output = output.replace(a, b)
    return output

def setup_analysis(name: str, author: str='', script: str=''):
    if not author:
        author_name, author_email = find_author()
    else:
        author_list = author.split()
        if len(author) == 1:
            author_name = author
        else:
            author_name, author_email = author_list
            author_email = author_email.replace('<', '').replace('>', '')
    replacement_dict = {
        '@@@ANALYSIS_NAME@@@': name,
        '@@@SCRIPT_NAME@@@': script,
        '@@@AUTHOR_NAME@@@': author_name,
        '@@@AUTHOR_EMAIL@@@': author_email
    }

    from os import mkdir
    from subprocess import getoutput
    path = getoutput('git rev-parse --show-toplevel') + '/analyses/' + name
    try:
        mkdir(path)
        mkdir(path + '/src')
        mkdir(path + '/include')
    except FileExistsError:
        pass
    try:
        with open(path + '/src/' + script + '.cc', 'w') as f:
            f.write(replace_all(source_tmpl, replacement_dict))
        with open(path + '/src/classes.h', 'w') as f:
            f.write(replace_all(class_tmpl, replacement_dict))
        with open(path + '/src/classes.xml', 'w') as f:
            f.write(replace_all(xml_tmpl, replacement_dict))
        with open(path + '/include/' + script + '.h', 'w') as f:
            f.write(replace_all(header_tmpl, replacement_dict))
    except OSError as error:
        print('FCCAnalysis space "' + name + '" creation error:')
        print(error)

