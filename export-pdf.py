

import subprocess
from atlassian import Confluence

confluence = Confluence(
  url="https://bxpress.atlassian.net/wiki", username="1", password="1",
  api_version="cloud"
)

'''
  padre conocido = xxx
    recupero todos los hijos
    guardo en dict
    por cada hijo busco sus descent (1 nivel)

'''

ids=[
# "586056468",
# "593299559",
# "663289857",
# "395609273",
# "613842945",
# "578159583",
# "310247747",
# "578224973",
# "562792407",
# "615350475",
# "308969527",
# "310510277",
# "607028044",
# "460357633",
# "613482802",
# "593395791",
# "613384306",
# "395609314",
# "308903979",
# "420806945",
# "490504964",
# "626622475",
# "310510294",
# "502726664",
# "502792252",
# "568328493",
# "576061497",
# "619807060",
# "395051009",
# "625705135",
# "663355400",
# "341213614",
# "543588369",
# "665419787",
# "665518105",
# "630128823",
# "576454737",
# "593297516",
# "593363602",
# "593363626",
# "593364124",
# "601391244",
# "605323269",
# "619118687",
# "625706218",
# "578290518",
# "340984239",
# "607060128",
# "625706442",
# "295010569",
# "613679156",
# "591102082",
# "409207153",
# "602931420",
# "602931486",
# "604405879",
# "604405888",
# "624525313",
# "625706462",
# "625640317",
# "625640324",
# "625640331",
# "625706576",
# "642941365",
# "625706490",
# "625706523",
# "625640350",
# "625706535",
# "625640375",
# "625706565",
# "628129958",
# "637894701",
# "384761925",
# "638779672",
# "642941437",
# "490505007",
# "304284011",
# "395641776",
# "395674709",
# "612761630",
# "521994322",
# "543588563",
# "324731234",
# "618889416",
# "607027973",
# "607126066",
# "381059073",
# "625607636",
# "625706252",
# "304382001",
# "530776110",
# "481067701",
# "530808869",
# "341049869",
# "341017314",
# "628359169",
# "634388790",
# "608927749",
# "607061240",
# "613908503",
# "340984559",
# "610664453",
# "395609424",
# "395674515",
# "395608204",
# "381157455",
# "613908496",
# "619413572",
# "395641474",
# "628490241",
"631046331",
"637993068",
"638255180",
"640057402",
"640975072",
"640909585",
"641695751",
"432439424",
"480542735",
"607126302",
"635175035",
"395576284",
"340984459",
"392986629",
"478216511",
"631275529",
"631046345",
"631046352",
"633208855",
"633208844",
"632783030",
"633176113",
"633274411",
"633602049",
"633569287",
"633634845",
"633569519",
"640155716",
"648380459",
"648511537",
"622788866",
"322928764",
"480542728",
"333381636",
"320831523",
"420807127",
"606502919",
"613384433",
"613482792",
"613351828",
"614367333",
"636158110",
"643694723",
"481099825",
"625640858",
"381190215",
"605716510",
"490537657",
"606404658",
"341049697",
"395642031",
"578192796",
"543588599",
"555155477",
"384761859",
"568328469",
"562792386",
"616661067",
"619053094",
"607093929",
"420413763",
"613842956",
"614924289",
"490537616",
"612663318",
"634290453",
"670433281",
"617545753",
"617742755",
"618856748",
"619380817",
"623018022",
"628293649",
"628392015",
"629374977",
"635568129",
"638386177",
"640352320"]
if __name__ == "__main__":
    space = "ARCHBX"
    # page_title = "Test"
    # page_id = confluence.get_page_id(space, page_title)

    # jq -r '.results[].id' 304316473.json
    
    for id in ids:
      content = confluence.export_page(str(id))
      with open("[Development-Guidelines]]_"+id+".pdf", "wb") as pdf_file:
        pdf_file.write(content)
        pdf_file.close()
        print("Completed:"+str(id))
        
      # Get all pages from Space
    # content_type can be 'page' or 'blogpost'. Defaults to 'page'
    # expand is a comma separated list of properties to expand on the content.
    # max limit is 100. For more you have to loop over start values.
    #pages = confluence.get_all_pages_from_space(space, start=0, limit=100, status="current", expand=None, content_type='page')
    # {'id': '114065640', 'type': 'page', 'status': 'current', 'title': 'Arquitectura BX', 'macroRenderedOutput': {}, 'extensions': {'position': 7}, '_expandable': {'container': '/rest/api/space/ARCHBX', 'metadata': '', 'restrictions': '/rest/api/content/114065640/restriction/byOperation', 'history': '/rest/api/content/114065640/history', 'body': '', 'version': '', 'descendants': '/rest/api/content/114065640/descendant', 'space': '/rest/api/space/ARCHBX', 'childTypes': '', ...}, '_links': {'self': 'https://bxpress.atlassian.net/wiki/rest/api/content/114065640', 'tinyui': '/x/6IDMBg', 'editui': '/pages/resumedraft.action?draftId=114065640', 'webui': '/spaces/ARCHBX/overview'}}
    # for page in pages:
    #   print(page["title"])

    # if(False):
    #   content = confluence.export_page(661946691)
    #   with open("output.pdf", "wb") as pdf_file:
    #       pdf_file.write(content)
    #       pdf_file.close()
    #       print("Completed")