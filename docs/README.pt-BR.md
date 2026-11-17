# Fixen UI Studio

[English — documentação principal](../README.md) · [Bahasa Indonesia](README.id.md) · [Español](README.es.md) · Português (Brasil) · [简体中文](README.zh-CN.md)

**Design com contexto de produto, interfaces funcionais e revisão visual com evidências.**

Fixen UI Studio é uma habilidade de código aberto para agentes de IA que projetam, implementam, avaliam e aprimoram interfaces web. O fluxo reúne descoberta do produto, direção de arte, UX, desenvolvimento frontend, revisão visual e busca opcional de imagens reais.

**v1.2.1 · Experimental.** O nome anterior era Fixenzo UI Studio. Use `$fixen-ui-studio` para invocar a habilidade. O pacote contém instruções Markdown/YAML; o agente hospedeiro fornece o modelo, as ferramentas e as permissões.

## Instalação

Baixe `fixen-ui-studio-v1.2.1.zip` em [GitHub Releases](https://github.com/riantosee/Fixen-ui-Studio/releases). Extraia a pasta `fixen-ui-studio/` no diretório de habilidades do Codex, de modo que o arquivo de entrada fique em:

```text
~/.codex/skills/fixen-ui-studio/SKILL.md
```

No Windows, `~` geralmente é a pasta do seu perfil. Se você configurou `CODEX_HOME`, use o diretório de habilidades dessa configuração. Faça backup das personalizações antes de substituí-las. Outra opção é clonar o repositório e copiar somente `skills/fixen-ui-studio/`. Nem todos os outros ambientes foram testados.

## Exemplos

```text
Use $fixen-ui-studio para criar um painel de despacho de entregas.
Priorize atrasos, filtros e ações claras para resolver problemas.
Use a tecnologia do projeto e dados sintéticos.
```

```text
Use $fixen-ui-studio para avaliar a hierarquia e a acessibilidade desta página.
Apresente evidências e recomendações práticas. Não altere arquivos.
```

```text
Use $fixen-ui-studio para uma interface de reservas com inglês como idioma
principal e versões em português e árabe. Reutilize o sistema i18n;
verifique preços, datas, layout móvel e navegação RTL.
```

## Idiomas e imagens

O inglês é o idioma principal da documentação. O agente deve se comunicar no idioma solicitado pelo usuário. O idioma da interface segue a direção do produto e as convenções do repositório. Em um produto novo sem orientação de idioma, use inglês e informe essa suposição. O [guia de localização](../skills/fixen-ui-studio/systems/localization.md) aborda formatos regionais, expansão de texto, fontes e RTL. A habilidade não instala um mecanismo de tradução nem garante qualidade em todos os idiomas.

A [busca de imagens](../skills/fixen-ui-studio/design/asset-sourcing.md) é opcional e depende das ferramentas disponíveis. Seleção, download, integração e verificação do resultado são etapas distintas. Um pedido de seleção termina nas recomendações. Registre fontes, autores, condições e verificações no [registro de recursos](../skills/fixen-ui-studio/templates/asset-register.md). Imagens de terceiros mantêm suas próprias licenças.

## Contribuição e validação

Consulte [CONTRIBUTING.md](../CONTRIBUTING.md), disponível em inglês. Traduções são bem-vindas; preserve identificadores, comandos, caminhos, o significado da licença e os limites das evidências. Se houver diferenças, consulte o [README em inglês](../README.md) e o [histórico de alterações](../CHANGELOG.md) e relate a divergência.

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s scripts -p "test_*.py" -v
```

As verificações para colaboradores exigem Python 3.10+; usar as instruções da habilidade não exige Python. A validação estrutural não comprova qualidade visual, qualidade de tradução, conformidade de acessibilidade nem superioridade em avaliações. Veja o [escopo da validação](validation.md). Os READMEs traduzidos não equivalem a testes de navegador em cada idioma.

## Segurança e licença

Exploração não autorizada, roubo de credenciais, injeção maliciosa de instruções, malware e ações destrutivas são proibidos nas contribuições e nos espaços da comunidade. Avaliações defensivas autorizadas com ambientes isolados e dados sintéticos são permitidas. Relate vulnerabilidades em particular conforme a [política de segurança](../SECURITY.md) e siga o [código de conduta](../CODE_OF_CONDUCT.md). A habilidade não é um sandbox nem garante proteção contra injeção de instruções.

A [licença MIT](../LICENSE) permite uso comercial, modificação, redistribuição e venda com a preservação dos avisos de direitos autorais e licença. As políticas de segurança e comunidade não alteram essas permissões nem autorizam ataques a outros sistemas. Forks devem informar a origem e as mudanças, sem se apresentar como versões oficiais.
