

from atlassian import Confluence

confluence = Confluence(
  url="https://bxpress.atlassian.net/wiki", username="a", password="b",
  api_version="cloud"
)

if __name__ == "__main__":
    space = "ARCHBX"
    # page_title = "Test"
    # page_id = confluence.get_page_id(space, page_title)

    # Get all pages from Space
    # content_type can be 'page' or 'blogpost'. Defaults to 'page'
    # expand is a comma separated list of properties to expand on the content.
    # max limit is 100. For more you have to loop over start values.
    pages = confluence.get_all_pages_from_space(space, start=0, limit=100, status="current", expand=None, content_type='page')
    # {'id': '114065640', 'type': 'page', 'status': 'current', 'title': 'Arquitectura BX', 'macroRenderedOutput': {}, 'extensions': {'position': 7}, '_expandable': {'container': '/rest/api/space/ARCHBX', 'metadata': '', 'restrictions': '/rest/api/content/114065640/restriction/byOperation', 'history': '/rest/api/content/114065640/history', 'body': '', 'version': '', 'descendants': '/rest/api/content/114065640/descendant', 'space': '/rest/api/space/ARCHBX', 'childTypes': '', ...}, '_links': {'self': 'https://bxpress.atlassian.net/wiki/rest/api/content/114065640', 'tinyui': '/x/6IDMBg', 'editui': '/pages/resumedraft.action?draftId=114065640', 'webui': '/spaces/ARCHBX/overview'}}
    for page in pages:
      print(page["title"])

    if(False):
      content = confluence.export_page(661946691)
      with open("output.pdf", "wb") as pdf_file:
          pdf_file.write(content)
          pdf_file.close()
          print("Completed")