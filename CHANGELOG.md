# CHANGELOG.md

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v2.0.0] - Unreleased

### Added

- CI/CD Tests
- Fluxo de redefinição de senha (Forgot Password Feature)
- Geração de Certificado Padronizado com melhoria no layout.
- URL de preview do certificado em modo de desenvolvimento.

### Changed

- Lógica de rotas e pontos agora está no módulo "core"
- Refatoração da API de mapas e do gerenciamento de *map pins* em páginas estáticas.  
- Redesign completo do banco de dados (versão 2): novos modelos e migrações revisadas.  
- Refatoração do módulo administrativo.  
- Criação de eventos com rotas dedicadas. 
- Módulo de inscrição e subscrição de eventos.  
- Melhora no layout da visualização de eventos participados no perfil.
- Melhora dos cards de eventos participados no perfil com botao de gerar certificado funcional e toast para confirmação de exclusão de inscrição em evento.

### Fixed

- Correção de erros no formulário de criação de eventos.  
- Correção de falhas antigas no sistema de inscrição.  
- Correção no filtro de rotas.  
- Ajustes na integração do mapa da cidade e parâmetros de localização.  

## [v1.1.0] - 2025-10-17

### Added

- Funcionalidade de Login e Registro
- (CI/CD) Deploy Automatizado sincronizado com a main.
- Upload do banco de dados mensalmente no server.

### Changed

- Reorganização da estrutura de pastas (módulos agora só incluem lógica de negócio).
- Centralização dos componentes do front-end na pasta templates, com padronização das subpastas por módulo.
- Melhorias e componentização da interface mobile: sidebar, botões, campos de entrada e toasts.  
- Atualização do cabeçalho (header) para usuários autenticados em dispositivos móveis.  
- Ajustes no aviso de direitos autorais.  

### Fixed

- Correção dos arquivos de configuração do server (Nginx, Docker).
- Correção da estrutura de pastas do server e scripts.
- Diversas correções de compatibilidade e sobreposição de layout.
- Correções em verificações do formulário de atualização de dados do usuário  

### Removed

- Remoção da pasta de uploads do versionamento
- Exclusão de arquivos de desenvolvimento obsoletos.  

---

## [v1.0.0] - 2023-12-04

### Added

- Primeira versão estável do projeto.  
- Estrutura inicial do backend em Django.  
- Modelos e migrações básicas de usuários, eventos e rotas.  
- Configuração de autenticação e painel administrativo.  
- Implementação das primeiras APIs e integração inicial com o frontend.  

---

[unreleased]: https://github.com/vzapalowski/projetocric-django/compare/development...main  
[v1.1.0]: https://github.com/vzapalowski/projetocric-django/releases/tag/v1.1.0  
[v1.0.0]: https://github.com/vzapalowski/projetocric-django/releases/tag/v1.0.0