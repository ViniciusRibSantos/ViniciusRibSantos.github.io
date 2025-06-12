import sys
from bs4 import BeautifulSoup
import requests

def process_html_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    project_boxes = soup.find_all('div', class_='project-box-contain')

    valid_projects = []

    for box in project_boxes:
        project_name_tag = box.find('h2')
        project_link_tag = box.find('p').find('a')

        if project_name_tag and project_link_tag and project_link_tag.has_attr('href'):
            project_name = project_name_tag.get_text(strip=True)
            project_url = project_link_tag['href']

            try:
                response = requests.get(project_url, timeout=5)
                if response.status_code == 200:
                    valid_projects.append({
                        'name': project_name,
                        'url': project_url
                    })
                else:
                    print(f"URL {project_url} returned status code {response.status_code}", file=sys.stderr)
            except requests.exceptions.RequestException as e:
                print(f"Error requesting URL {project_url}: {e}", file=sys.stderr)

    if not valid_projects:
        return ""

    new_html_content = """<!doctype html>
<html lang="pt-br">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
    integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
  <link rel="stylesheet" href="css/style.css" />
  <title>Home</title>
</head>
<body>
  <div class="container">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="index.html">ViniciusRibSantos</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a class="nav-link" href="index.html"><i class="fas fa-home"></i></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="cv.html">CV</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="projetos.html">Meus Projetos</a>
          </li>
        </ul>
      </div>
    </nav>
    <div class="container">"""

    for project in valid_projects:
        new_html_content += f"""
      <div class="row project-box-contain">
        <div class="col-12 project-box">
          <h2>{project['name']}</h2>
          <p>Cotém os exercicios da materia Arquitetura de Software do Bacharelado em Ciencias da Computação. <a
              href="{project['url']}"><i class="fas fa-link"></i></a> </p>
        </div>
      </div>"""

    new_html_content += """
    </div>
    <div class="row">
      <div class="col-12 footer">
        <a href="https://www.linkedin.com/in/vinicius-ribeiro-662863136/">
          <i class="fab fa-linkedin fa-2x"></i>
        </a>
        <a href="https://github.com/ViniciusRibSantos">
          <i class="fab fa-github fa-2x"></i>
        </a>
      </div>
    </div>
  </div>
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
    crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
    integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
    crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
    crossorigin="anonymous"></script>
</body>
</html>"""
    return new_html_content

if __name__ == '__main__':
    try:
        with open("projetos.html", "r", encoding="utf-8") as f:
            original_html = f.read()

        processed_html = process_html_content(original_html)
        print(processed_html)

    except FileNotFoundError:
        print("Error: projetos.html not found.", file=sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
