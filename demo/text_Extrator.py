import re


path  = 'C:\Thameem\POC_CODE\pdf_txt.txt'

def pdf_txt_preprocessing(path):
    file = open(path, 'r', encoding="utf8",errors='ignore').readlines()

    lst=[i.encode('utf8','ignore').decode("utf8").strip() for i in file if i!=""]
    lst = [re.sub("\s+"," ",i) for i in lst]

    ToC_list = ['Contents', 'Preface', 'Conventions Used in This Book', '1 Introducing Oracle NoSQL Database Security', '2 Security Configuration', 'Security Configuration Overview', 'Configuring Security with Makebootconfig', 'Configuring Security with Securityconfig', 'Creating the security configuration', 'Adding the security configuration', 'Verifying the security configuration', 'Updating the security configuration', 'Showing the security configuration', 'Removing the security configuration', 'Merging truststore configuration', '3 Performing a Secure Oracle NoSQL Database Installation', 'Single Node Secure Deployment', 'Adding Security to a New Installation', 'Adding Security to an Existing Installation', 'Multiple Node Secure Deployment', 'Adding Security to a New Installation', 'Adding Security to an Existing Installation', '4 Kerberos Authentication Service', 'Installation Prerequisites', 'Kerberos Principal', 'Keytabs', 'Kadmin and kadmin.local', 'Kerberos Security Properties', 'Setting Security Properties in a security login file', 'Setting Security Properties through KVStoreConfig', 'Using Security Properties to Log In', 'Using credential cache', 'Using a keytab', 'JAAS programming framework integration', 'Performing a Secure Oracle NoSQL Database Installation with Kerberos', 'Adding Kerberos to a New Installation', 'Adding Kerberos to an Existing Secure Installation', 'Using Oracle NoSQL Database with Kerberos and Microsoft Active Directory (AD)', '5 External Password Storage', 'Oracle Wallet', 'Password store file', '6 Security.xml Parameters', 'Top-level parameters', 'Transport parameters', '7 Encryption', 'SSL model', 'SSL communication properties', 'Disk Encryption in a Linux Environment', '8 Configuring Authentication', 'User Management', 'User Creation', 'User Modification', 'User Removal', 'User Status', 'User Login', 'Password Management', 'Sessions', '9 Configuring Authorization', 'Privileges', 'System Privileges', 'Object Privileges', 'Table Ownership', 'Privilege Hierarchy', 'Roles', 'System Built-in Roles', 'User-Defined Roles', 'Managing Roles, Privileges and Users', 'Role Creation', 'Role Removal', 'Role Status', 'Grant Roles or Privileges', 'Revoke Roles or Privileges', '10 Security Policies', 'Security Policy Modifications', '11 Audit Logging', 'Security Log Messages', '12 Keeping Oracle NoSQL Database Secure', 'Guidelines for Securing the Configuration', 'Guidelines for Deploying Secure Applications', 'Guidelines for Securing the SSL protocol', 'Guidelines for using JMX securely', 'Guidelines for Updating Keystore Passwords', 'Guidelines for Updating Kerberos Passwords', 'Guidelines for Updating SSL Keys and Certificates', 'Guidelines for Configuring External Certificates for a new Installation', 'Guidelines for Configuring External Certificates for an Existing Default Secure Installation', 'Guidelines for Updating the External Certificates', 'Guidelines for Operating System Security', 'A Password Complexity Policies', 'B SSL keystore generation', 'C Java KeyStore Preparation', 'Import Key Pair to Java Keystore', 'D KVStore Required Privileges', 'Privileges for Accessing CLI Commands', 'Privileges for DDL Commands', 'Privileges for Accessing KVStore APIs', 'Privileges for Accessing KVStore TableAPIs', 'Privileges for Accessing KvLargeObject APIs', 'E Configuring the Kerberos Administrative Utility', 'F Manually Registering Oracle NoSQL Database Service Principal', 'G Third Party Licenses']

    lst =[i for i in lst  if re.search("[A-Za-z]{3,}",i) and i not in ToC_list]

    lst2 = " ".join([re.sub("'|\"|\\\\","",x) for x in lst])
    return processed_txt

print(pdf_txt_preprocessing(path))









# import string,re
# file = open('info.txt', 'r', encoding="utf8")
# tokens =file.read()
# re_punc = re.compile('[%s]' % re.escape(string.punctuation))
# word_tokens = [re_punc.sub('', w) for w in tokens]
# print(word_tokens)
