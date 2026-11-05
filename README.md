# web-e2e-behave-selenium

![E2E Tests](https://github.com/MateusCerqueiraG/web-e2e-behave-selenium/actions/workflows/e2e.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4-43B02A?logo=selenium&logoColor=white)
![Behave](https://img.shields.io/badge/BDD-Behave-0A7BFF?logo=cucumber&logoColor=white)

Automação de testes **Web end-to-end** com **Python + Behave (BDD) + Selenium WebDriver**, seguindo o **Page Object Model**, rodando **cross-browser** (Chrome e Firefox) e em **CI (GitHub Actions)** com relatório **Allure**.

> **Alvo sob teste:** [SauceDemo](https://www.saucedemo.com) — aplicação de e-commerce **pública, feita para prática de QA**. Nenhum sistema real ou privado é tocado.

## O que a suíte cobre
- **Login** — caminho feliz, usuário bloqueado (`locked_out_user`) e validação de campo obrigatório
- **Carrinho** — adicionar/remover item e contagem do badge
- **Checkout** — compra ponta a ponta + cenário negativo (dados obrigatórios)

## Técnicas e boas práticas demonstradas
- Cenários em **Gherkin** (`.feature`) — BDD legível por negócio
- **Page Object Model** — `pages/` separado de `steps/`, com `BasePage` e esperas explícitas
- **Cross-browser** via variável `BROWSER` (`chrome` | `firefox`), headless no CI
- **Screenshot anexado ao Allure** automaticamente quando um passo falha
- **GitHub Actions** com matriz (Chrome + Firefox) a cada push

## Estrutura
```
web-e2e-behave-selenium/
├── features/
│   ├── environment.py          # ciclo de vida do driver, cross-browser, screenshot on-fail
│   ├── login.feature
│   ├── cart.feature
│   ├── checkout.feature
│   ├── pages/                  # Page Object Model
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   └── steps/                  # implementação dos passos Gherkin
│       ├── common_steps.py
│       ├── login_steps.py
│       ├── cart_steps.py
│       └── checkout_steps.py
├── .github/workflows/e2e.yml   # CI matriz Chrome + Firefox
├── behave.ini
└── requirements.txt
```

## Como rodar localmente
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

behave                     # Chrome, headless (padrão)
BROWSER=firefox behave     # Firefox
HEADLESS=false behave      # abre o navegador pra você ver
```
> Selenium 4 gerencia os drivers automaticamente (Selenium Manager) — não precisa baixar chromedriver/geckodriver.

## Relatório Allure

**Local:**
```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results
allure serve allure-results
```

**Publicado (GitHub Pages):** a cada push na `main`, o CI gera o relatório Allure (Chrome + Firefox, com histórico) e publica em:

👉 **https://mateuscerqueirag.github.io/web-e2e-behave-selenium/**

> Disponível após tornar o repositório **público** e habilitar o Pages em *Settings → Pages → Deploy from a branch → `gh-pages` / root*.

## CI
Cada push roda a suíte em **Chrome e Firefox** no GitHub Actions (aba *Actions*). O badge no topo reflete o último resultado.

---
*Projeto de portfólio — foco em automação Web E2E com BDD. Alvo exclusivamente o app público de demonstração SauceDemo.*
