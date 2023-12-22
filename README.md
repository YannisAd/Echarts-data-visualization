<a name="readme-top"></a>




<!-- PROJECT LOGO -->
<br />
<div align="center">
  

  <h3 align="center">OmekaToRdf Documentation</h3>

  <p align="center">
    <br />
    <a href="https://github.com/nlasolle/omekas2rdf"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://videos.ahp-numerique.fr/w/uy6SWhsPq2T8QQCyx92CEK">View Demo</a>
    ·
    <a href="https://github.com/nlasolle/omekas2rdf/issues">Report Bug</a>
    ·
    <a href="https://github.com/nlasolle/omekas2rdf/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#installation">Installation</a>
      <ul>
        <li><a href="#ZIP-download">Download ZIP</a></li>
        <li><a href="#Clone-repository">Clone repository</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#run-on-server">Run on server </a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



This Python script has been created for the daily export of an Omeka S database to an RDF database (Turtle syntax).

Omeka S is a CMS (Content Management System) dedicated to the editing and the publishing of collections. It allows to create elements and publish them on a website based on the use of blocks and modules. Is is particularly adapted for cultural heritage collections (museums, archive places, libraries, etc).

It is currently in use for a project dedicated to Henri Poincaré (1854-1912), famous French man of science, managed by the Archives Henri-Poincaré laboratory. The website is available at http://henripoincare.fr.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][Python-url]][Python.py]



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->

### Installation

This guide will help you download the Omekas2RDF project locally on your computer. You can choose between two methods: directly download the file or clone the GitHub repository.



### ZIP-download

1. At the top right of the page click on the green “Code” button.
2. Select “Download ZIP”.
3. Once the download is complete, extract the contents of the ZIP file to the folder of your choice on your computer.


### Clone-repository


1. Open a terminal or command prompt on your computer.
2. Make sure you have Git installed. If not, you can download it [here](https://github.com/git-guides/install-git) and follow the installation instructions.
3. In the terminal, run the following command:

```sh
git clone https://github.com/nlasolle/omekas2rdf.git
```

Once the command is executed, the repository will be cloned into a folder called "omekas2rdf" in the directory you are located in.


<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- USAGE EXAMPLES -->
## Usage

<table>
  <tr>
    <th>Fichier</th>
    <th>Méthode / Fonction</th>
    <th>Adaptations pour Votre Projet</th>
    <th>Dépendances à Installer</th>
  </tr>
  <tr>
    <td rowspan="19"><strong>omekaToRDF.py</strong></td>
    <td>alterFilesPermissions()</td>
    <td>Configurer les répertoires selon votre système (<code>FILES_REPOSITORY</code>, <code>BACKUP_REPOSITORY</code>, <code>LOGS_REPOSITORY</code>)</td>
    <td rowspan="7">
      <ul>
        <li><code>requests</code> pour les appels à l'API</li>
        <li><code>rdflib</code> pour manipuler les données RDF</li>
        <li><code>os</code> pour les opérations sur les fichiers et répertoires</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>createBackup()</td>
    <td>Ajuster le chemin pour stocker les sauvegardes (<code>BACKUP_REPOSITORY</code>)</td>
  </tr>
  <tr>
    <td>cleanRepository()</td>
    <td>Configurer la durée de conservation des fichiers anciens (<code>MAX_DAYS</code>)</td>
  </tr>
  <tr>
    <td>configureLogging()</td>
    <td>Configurer l'emplacement des fichiers de logs (<code>LOGS_REPOSITORY</code>)</td>
  </tr>
  <tr>
    <td>saveNamespaces()</td>
    <td>Ajuster l'URL de l'API Omeka S (<code>API_PATH</code>)</td>
  </tr>
  <tr>
    <td>saveResources()</td>
    <td>Ajuster l'URL de l'API et configurer selon les ressources nécessaires</td>
  </tr>
  <tr>
    <td rowspan="9"><strong>constants.py</strong></td>
    <td>N/A (fichier de constantes)</td>
    <td>Adapter les constantes liées aux chemins et à la configuration du CMS Omeka S</td>
    <td>Aucune dépendance externe spécifique</td>
  </tr>
  <tr>
    <td rowspan="5"><strong>triplesCreation.py</strong></td>
    <td>initializeRDFdatabase()</td>
    <td>Configurer les espaces de noms pour les propriétés RDF</td>
    <td rowspan="4">
      <ul>
        <li><code>rdflib</code> pour manipuler les données RDF</li>
        <li><code>os</code> pour les opérations sur les fichiers et répertoires</li>
      </ul>
    </td>
  </tr>


  <tr>
    <td rowspan="5"><strong>triplesCreation.py</strong></td>
    <td>initializeRDFdatabase()</td>
    <td>Configurer les espaces de noms pour les propriétés RDF</td>
    <td rowspan="4">
      <ul>
        <li><code>rdflib</code> pour manipuler les données RDF</li>
        <li><code>os</code> pour les opérations sur les fichiers et répertoires</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>saveGraphToFile()</td>
    <td>Configurer le chemin du fichier de sortie RDF</td>
  </tr>
  <tr>
    <td>createItemsTriples()</td>
    <td>Configurer les espaces de noms pour les propriétés RDF des éléments</td>
  </tr>
  <tr>
    <td>createMediasTriples()</td>
    <td>Configurer les espaces de noms pour les propriétés RDF des médias</td>
  </tr>
  <tr>
    <td>createCollectionsTriples()</td>
    <td>Configurer les espaces de noms pour les propriétés RDF des collections</td>
  </tr>



<tr>
    <td rowspan="9"><strong>constants.py</strong></td>
    <td>N/A (fichier de constantes)</td>
    <td>Adapter les constantes liées aux chemins et à la configuration du CMS Omeka S</td>
    <td>Aucune dépendance externe spécifique</td>
  </tr>
  <tr>
    <td colspan="3"><em>Il n'y a pas de fonctions spécifiques dans ce fichier. Il contient principalement des constantes utilisées dans les autres fichiers du projet.</em></td>
  </tr>

</table>





<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png

[Python.py]: https://www.python.org/

[python-url]: https://www.python.org/static/community_logos/python-logo.png

[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
