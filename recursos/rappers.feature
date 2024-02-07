Feature: Reproduzir os videos dos melhores Rappers

  @video
  Scenario: Localizar os videos dos melhores rappers
    Given que acesso o site
    When preencho o campo de pesquisa
    | rappers | video |
    | eminem | clean out my closet |
    | snoop dogg | still dre |
    | 2 pac | ambitions |
    Then o video é selecionado