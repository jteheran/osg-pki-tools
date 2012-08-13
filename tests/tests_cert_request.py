"""Test cert-request script"""

import re

import PKIClientTestCase

class CertRequestTests(PKIClientTestCase.PKIClientTestCase):

    command = "osg-cert-request"

    def test_help(self):
        """Test running with -h to get help"""
        result = self.run_script(self.command, "-h")
        err_msg = self.run_error_msg(result)
        self.assertEqual(result.returncode, 0, err_msg)
        self.assertTrue("Usage:" in result.stdout, err_msg)

    def test_request(self):
        """Test making a request"""
        fqdn = "test." + self.domain
        result = self.run_script(self.command,
                                 # TODO: Good hostname for testing?
                                 "--hostname", fqdn,
                                 "-e", self.email,
                                 "-n", self.name,
                                 "-p", self.phone)
        err_msg = self.run_error_msg(result)
        self.assertEqual(result.returncode, 0, err_msg)
        match = re.search("^Request Id#: (\d+)\s*$",
                          result.stdout,
                          re.MULTILINE)
        self.assertNotEqual(match, None,
                            "Could not find request Id: " + err_msg)

