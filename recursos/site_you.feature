Feature: site Youtube

  @you
  Scenario: acessar o site youtube
    Given que acesso o https://www.youtube.com
    When preencho o campo de pesquisa com 50cent e clico em pesquisar
    Then é exibido o resultado da pesquisa e o titulo da pagina é 50cent - YouTube

  @video
  Scenario: Localizar os videos dos melhores rappers
    Given que acesso o https://www.youtube.com
    When preencho o campo de pesquisa
    | rappers | video |
    | eminem | clean out my closet |
    | snoop dogg | still dre |
    | 2 pac | ambitions |
    Then o video é selecionado