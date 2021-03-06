import sys
import os
if sys.version_info > (3, 0):
    from io import StringIO
else:
    from StringIO import StringIO
from ensembler.utils import get_installed_resource_filename
import ensembler.pdb
from mock import Mock
from nose.plugins.attrib import attr


@attr('unit')
def test_extract_residues_by_resnum_from_4CFE():
    # 4CFE contains a 'TPO' residue
    pdb_input_filepath = get_installed_resource_filename(os.path.join('tests', 'resources', '4CFE.pdb.gz'))
    template = Mock()
    template.chainid= 'A'
    template.resolved_pdbresnums = [str(x) for x in range(16, 269)]
    ofile = StringIO()
    ensembler.pdb.extract_residues_by_resnum(ofile, pdb_input_filepath, template)
    ofile.close()


@attr('unit')
def test_extract_residues_by_resnum_from_3HLL():
    # 3HLL contains resnums '56A' and '93B'
    pdb_input_filepath = get_installed_resource_filename(os.path.join('tests', 'resources', '3HLL.pdb.gz'))
    template = Mock()
    template.chainid = 'A'
    template.resolved_pdbresnums = [str(x) for x in range(24, 172) + range(183, 309)]
    template.resolved_pdbresnums[template.resolved_pdbresnums.index('56')] = '56A'
    template.resolved_pdbresnums[template.resolved_pdbresnums.index('93')] = '93B'
    ofile = StringIO()
    ensembler.pdb.extract_residues_by_resnum(ofile, pdb_input_filepath, template)
    ofile.close()


@attr('unit')
def test_extract_residues_by_resnum_output():
    pdb_input_filepath = get_installed_resource_filename(os.path.join('tests', 'resources', '3HLL.pdb.gz'))
    template = Mock()
    template.chainid = 'A'
    template.resolved_pdbresnums = [str(x) for x in range(24, 172) + range(183, 309)]
    template.resolved_pdbresnums[template.resolved_pdbresnums.index('56')] = '56A'
    template.resolved_pdbresnums[template.resolved_pdbresnums.index('93')] = '93B'
    ofile = StringIO()
    ensembler.pdb.extract_residues_by_resnum(ofile, pdb_input_filepath, template)
    ofile_text = ofile.getvalue()
    first_line = ofile_text[0: ofile_text.index('\n')]
    assert first_line == 'ATOM    175  N   TYR A  24      50.812  43.410  19.390  1.00 38.55           N  '
    ofile.close()
