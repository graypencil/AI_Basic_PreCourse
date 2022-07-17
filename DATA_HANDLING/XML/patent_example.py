import urllib.request
from bs4 import BeautifulSoup

with open("US08621662-20140107.xml", "r", encoding="UTF8") as patent_xml:
    xml = patent_xml.read()

soup = BeautifulSoup(xml, "lxml")

invention_title_tag = soup.find("invention-title")
print(invention_title_tag.get_text())

# xml의 구조적인 정보도 알아야 정보를 추출할 수 있음
publication_reference_tag = soup.find("publication-reference")
p_document_id_tag = publication_reference_tag.find("document-id")
p_country = p_document_id_tag.find("country").get_text()
p_doc_number = p_document_id_tag.find("doc-number").get_text()
p_kind = p_document_id_tag.find("kind").get_text()
p_date = p_document_id_tag.find("date").get_text()

print(p_doc_number, p_kind, p_date)

application_reference_tag = soup.find("application-reference")
a_document_id_tag = publication_reference_tag.find("document-id")
a_country = p_document_id_tag.find("country").get_text()
a_doc_number = p_document_id_tag.find("doc-number").get_text()
a_date = p_document_id_tag.find("date").get_text()

print(a_country, a_doc_number, a_date)