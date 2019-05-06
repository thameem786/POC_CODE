import nltk


# # s_list = [
#     "SAP HANA - DATA REPLICATION",
#     "SAP HANA Replication allows migration of data from source systems to SAP HANA database.",
#     "SAP HANA ETL based replication uses SAP Data Services to migrate data from SAP or nonSAP source system to target HANA database.",
#     "How to use SAP HANA Data Services ETL based Replication?",
#     "SAP HANA SAP HANA - ETL BASED REPLICATION SAP HANA SAP HANA - ETL BASED REPLICATION Login to Data Services Designer (choose Repository) -> Create Data store",
#     "SAP HANA",
#     "SAP HANA",
#     "SAP HANA",
#     "SAP HANA",
#     "Create Data store-> Name of data store SAP_HANA_TEST ->Data store type (database) -> Database type SAP HANA -> Database version HANA 1.x.",
#     "The main components of this replication method are the Sybase Replication Agent, which is part of the SAP source application system, Replication agent and the Sybase Replication Server that is to be implemented in SAP HANA system.",
#     "SAP HANA SAP HANA - LOG BASED REPLICATION SAP HANA SAP HANA - LOG BASED REPLICATION Initial Load in Sybase Replication method is initiated by Load Controller and triggered by the administrator, in SAP HANA.",
#     "R3 load on target system imports data into SAP HANA database.",
#     "SAP HANA",
#     "SAP HANA",
#     "SAP HANA",
#     "SAP HANA",
#     "This method was part of initial offering for SAP HANA replication, but not positioned/supported anymore due to licensing issues and complexity and also SLT provides the same features.",
#     "Direct Extractor Connection data replication reuses existing extraction, transformation, and load mechanism built into SAP Business Suite systems via a simple HTTP(S) connection to SAP HANA.",
#     "This method requires no additional server or application in the SAP HANA system landscape.",
#     "DXC method reduces complexity of data modeling in SAP HANA as data sends to HANA after applying all business extractor logics in Source System.",
#     "It speeds up the time lines for SAP HANA implementation project",
#     "SAP HANA SAP HANA - DXC METHOD SAP HANA SAP HANA - DXC METHOD",
#     "SAP HANA",
#     "SAP HANA",
#     "SAP HANA",
#     "SAP HANA",
#     "It provides semantically rich data from SAP Business Suite to SAP HANA",
#     "It reuses existing proprietary extraction, transformation, and load mechanism built into SAP business Suite systems over a simple HTTP(S) connection to SAP HANA.",
#     "Setup SAP HANA Direct Extractor Connection: Download the DXC delivery unit into SAP HANA.",
#     "Import the unit using Import Dialog in SAP HANA Content Node -> Configure XS Application server to utilize the DXC -> Change the application_container value to libxsdxc",
#     "Open SAP HANA Studio -> Create Schema under Catalog tab.",
#     "SAP HANA SAP HANA - CTL METHOD SAP HANA SAP HANA - CTL METHOD -----------------------------------------",
#     "SAP HANA",
#     "SAP HANA",
#     "SAP HANA",
#     "SAP HANA",
#     "MDX Provider is used to connect MS Excel to SAP HANA database system.",
#     "SAP HANA supports both query languages: SQL and MDX.",
#     "Excel Pivot tables use MDX as query language to read data from SAP HANA system.",
#     "SAP HANA SAP HANA - MDX PROVIDER SAP HANA SAP HANA - MDX PROVIDER MDX provider enables the consumption of Information views defined in HANA studio by SAP and non- SAP reporting tools.",
#     "SAP HANA",
#     "SAP HANA",
#     "SAP HANA",
#     "SAP HANA",
#     "Once you choose SAP HANA MDX provider from the list of data source you want to connect, pass HANA system details like host name, instance number, user name and password.",
#     "SAP HANA",
#     "Once installation of HANA client is done, you will see the option of SAP HANA MDX provider in the list of data source in MS Excel." ]
#

s_list = ["what is the purpose of quasar"]

new_s_list = []
for s in s_list:
    text = nltk.word_tokenize(s)
    print(text)
    # print(nltk.pos_tag(text))
    tag_tuple_list = nltk.pos_tag(text)
    print(tag_tuple_list)
    verb_found = False
    for word, tag in tag_tuple_list:
        if tag.startswith("VB"):
            verb_found = True
            print ("WORD- {} \t\t TAG- {}".format(word, tag))

    if verb_found is True:
#         print (s)
        new_s_list.append(s)


new_s_list = new_s_list[:5]
for s in new_s_list:
    print (s)

