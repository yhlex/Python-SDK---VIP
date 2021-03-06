import unittest
from suds.client import Client
import sys
sys.path.append("/Users/hanlinye/Desktop/Securitas-authenticateUserStub2/")

from symantec_package.lib.managementService.SymantecManagementServices import SymantecManagementServices
from symantec_package.HTTPHandler import setConnection, HTTPSClientAuthHandler, HTTPSClientCertTransport

class TestUserManagement(unittest.TestCase):
    def setUp(self):
        # the URLs for now which will have the WSDL files and the XSD file
        query_services_url = 'http://webdev.cse.msu.edu/~yehanlin/vip/vipuserservices-query-1.7.wsdl'
        userservices_url = 'http://webdev.cse.msu.edu/~morcoteg/Symantec/WSDL/vipuserservices-auth-1.7.wsdl'
        managementservices_url = 'http://webdev.cse.msu.edu/~huynhall/vipuserservices-mgmt-1.7.wsdl'

        # initializing the Suds clients for each url, with the client certificate youll have in the same dir as this file
        management_client = Client(managementservices_url,
                                   transport=HTTPSClientCertTransport('vip_certificate.crt', 'vip_certificate.crt'))

        self.test_management_services_object = SymantecManagementServices(management_client)

    # def test_create_user(self):
    #     user = self.test_management_services_object.createUser("new_user456", "new_user2")
    #     self.assertTrue("0000" in str(user))

    #     user2 = self.test_management_services_object.createUser("new_user456", "new_user2")
    #     self.assertTrue("6002" in str(user2))
    #     pass

    # def test_delete_user(self):
    #     user = self.test_management_services_object.deleteUser("delete_user123", "new_user2")
    #     self.assertTrue("0000" in str(user))

    #     user2 = self.test_management_services_object.deleteUser("delete_user456", "new_user2")
    #     self.assertTrue("6003" in str(user2))
    #     pass

    # def test_add_and_delete_STANDARD_OTP_credential(self):
    #     user = self.test_management_services_object.createUser("new_user456", "new_user3")
    #     self.assertTrue("0000" in str(user))

    #     otp_credential = self.test_management_services_object.addCredential("new_otp_cred", "new_user3", "VSTZ39646177", "STANDARD_OTP",\
    #                                                                         "672192")       #change with what's on your device
    #     self.assertTrue("0000" in str(otp_credential))

    #     deleted = self.test_management_services_object.removeCredential("remove_123", "new_user3", "VSTZ39646177",
    #                                                                     "STANDARD_OTP")
    #     self.assertTrue("0000" in str(deleted))

    #     user = self.test_management_services_object.deleteUser("delete_user123", "new_user3")
    #     self.assertTrue("0000" in str(user))
    #     pass

    
    def test_register_sms(self):
        # user = self.test_management_services_object.createUser("new_user456", "new_user7")
        # self.assertTrue("0000" in str(user))
        # self.test_management_services_object.removeCredential("1245442","y1196293","15177757651","SMS_OTP")
        # res = self.test_management_services_object.registerBySMS("123354","15177757651")
        # self.assertTrue("0000" in str(res))
        #self.test_management_services_object.addCredential("Add_credentail","y1196293","15177757651","SMS_OTP","309112")
        # user = self.test_management_services_object.deleteUser("delete_user123", "new_user3")
        # self.assertTrue("0000" in str(user))
        pass

# VOICE DOESNT WORK IN VIP MANAGER YET
    # def test_register_voice(self):
    #     res = self.test_management_services_object.registerByVoice("135434","15177757651")



if __name__ == '__main__':
    unittest.main()




