# TICKETS - IMPLEMENTAÇÃO SISTEMA PROTOCOLOS IPMA

---

## TICKET #1
### PROTOCOLOS: Sistema - Configuração inicial Odoo 17 com resolução de dependências

**Descrição do Problema:**

Durante a instalação do Odoo 17 clonado do repositório oficial Git, ocorreu erro `ModuleNotFoundError: No module named 'pkg_resources'` ao executar odoo-bin. O problema foi causado pela versão mais recente do setuptools (82.0.0) que removeu o módulo pkg_resources, essencial para o funcionamento do Odoo.

**Solução Implementada:**

- Criado ambiente virtual Python em `/opt/odoo/odoo17/venv/`
- Downgrade do setuptools para versão **67.8.0** (última versão com pkg_resources)
- Instalação de todas as dependências do `requirements.txt`
- Instalação adicional de **openpyxl** (3.1.5) para suporte Excel
- Instalação de **xlsxwriter** para geração de relatórios Excel
- Configuração de serviço systemd (`odoo17.service`) para execução automática
- Odoo 17 operacional em `http://192.168.156.117:8069`

---

## TICKET #2
### PROTOCOLOS: Sistema - Configuração PostgreSQL e dados de acesso

**Descrição do Problema:**

Necessidade de configurar base de dados PostgreSQL dedicada para o sistema de protocolos, com utilizador específico e credenciais seguras para separação de privilégios e melhor controlo de acesso.

**Solução Implementada:**

- Criado utilizador PostgreSQL `root` com privilégios de superuser
- Credencial configurada: `8kEZ^9I32r&£`
- Configuração em `/etc/odoo17.conf`:
  - `db_host = localhost`
  - `db_user = root`
  - `db_password = 8kEZ^9I32r&£`
  - `admin_passwd = Admin@PROTOCOLO2026!`
- Permissões do ficheiro de configuração ajustadas (`chmod 640`)
- Configurado **2 workers** para melhor performance
- PostgreSQL 16.11 operacional e integrado com Odoo

---

## TICKET #3
### PROTOCOLOS: Sistema - Reverse Proxy Apache para acesso via DNS sem porta

**Descrição do Problema:**

O utilizador solicitou acesso ao sistema através do DNS `protocolos.ipma.pt` sem necessidade de especificar porta (`:8069`) no URL. Adicionalmente, existia uma aplicação PHP legada em `/protocolos/` que deveria continuar acessível.

**Solução Implementada:**

- Criado VirtualHost Apache em `/etc/apache2/sites-available/protocolos-odoo.conf`
- Configurado `ProxyPass` para reencaminhar tráfego HTTP → Odoo:8069
- Adicionada exceção `ProxyPass` para `/protocolos/` (mantém acesso a aplicação PHP)
- Configurados cabeçalhos `X-Forwarded-*` para preservar IP real do cliente
- Restrição de acesso à rede interna: `192.168.156.0/24`
- Módulos Apache ativados: `proxy`, `proxy_http`, `headers`, `rewrite`
- Desativado `000-default.conf` para evitar conflitos
- **Resultado:**
  - `http://protocolos.ipma.pt/` → Odoo 17
  - `http://protocolos.ipma.pt/protocolos/` → Aplicação PHP legada

---

## TICKET #4
### PROTOCOLOS: Sistema - Integração e verificação LDAP para autenticação

**Descrição do Problema:**

Necessidade de integrar autenticação LDAP com servidor corporativo para permitir que utilizadores IPMA acedam ao sistema com as suas credenciais de domínio, evitando gestão duplicada de passwords.

**Solução Implementada:**

- Instalado **python-ldap 3.4.4** no virtual environment
- Verificada conectividade ao servidor LDAP: `192.168.150.231:389`
- Testado LDAP bind anónimo com sucesso
- Instalado módulo `auth_ldap` do Odoo 17 (adicionado como dependência)
- Criada infraestrutura para auto-atribuição de grupos (ver Ticket #6)
- **Estado:** Conectividade verificada, aguarda configuração de Base DN e credenciais de admin LDAP para configuração completa na interface Odoo

---

## TICKET #5
### PROTOCOLOS: Sistema - Criação de grupos de acesso e permissões por funções

**Descrição do Problema:**

Sistema requer controlo de acesso granular com 3 níveis de permissões para o módulo `ipma_protocolo`:

1. Utilizadores LDAP novos → apenas leitura (segurança por defeito)
2. Gestores de protocolos → acesso total CRUD
3. Utilizadores normais → apenas leitura

**Solução Implementada:**

- Criado ficheiro `data/groups.xml` com 3 grupos `res.groups`:
  - `group_ldap_readonly` - LDAP Users (Read-Only)
  - `group_protocolo_manager` - Protocol Managers (Full Access)
  - `group_protocolo_user` - Protocol Users (Read-Only)
- Configurados `ir.model.access` para cada grupo:
  - **LDAP readonly:** `perm_read=1`, outros=0
  - **Managers:** `perm_read=1`, `perm_write=1`, `perm_create=1`, `perm_unlink=1`
  - **Users:** `perm_read=1`, outros=0
- Atualizado `__manifest__.py` para incluir `'data/groups.xml'`
- Todos os grupos herdam de `base.group_user` (acesso básico Odoo)
- **Commit Git:** `591bb2f`

---

## TICKET #6
### PROTOCOLOS: Sistema - Auto-atribuição de grupo LDAP em primeiro login

**Descrição do Problema:**

Para evitar trabalho manual de atribuir grupo a cada novo utilizador LDAP, sistema deveria automaticamente adicionar novo utilizador ao grupo read-only na primeira autenticação, garantindo segurança por defeito.

**Solução Implementada:**

- Criado ficheiro `models/res_users.py` extendendo modelo `res.users`
- Implementado override do método `_auth_ldap()` que:
  - Intercepta autenticação LDAP bem-sucedida
  - Verifica se utilizador já tem grupo `group_ldap_readonly`
  - Auto-adiciona ao grupo se não existir (sem duplicações)
  - Validação robusta (não falha se grupo não existir)
- Atualizado `models/__init__.py` para importar novo módulo
- Atualizado `__manifest__.py`:
  - Versão incrementada para **17.0.1.1.0**
  - Adicionada dependência `'auth_ldap'`
- **Commit Git:** `fb3f32d`
- Sistema reiniciado para carregar novo comportamento

---

## CONFIGURAÇÃO GIT

Configurado repositório Git com identidade:

- **Nome:** Lucas Dias
- **Email:** lucas.dias@ipma.pt
- **Commits realizados:** `591bb2f`, `fb3f32d`

---

## ESTADO ATUAL DO SISTEMA

### ✅ OPERACIONAL

- Odoo 17 a correr em `http://protocolos.ipma.pt` (porta 8069 oculta)
- PostgreSQL configurado e funcional
- Apache reverse proxy ativo
- Grupos de acesso criados e carregados
- Auto-atribuição LDAP implementada
- Aplicação PHP legada mantida em `/protocolos/`

### ⏳ PENDENTE

- Configuração LDAP completa na interface Odoo (aguarda Base DN + credenciais)
- Atribuição manual de utilizadores existentes aos grupos Manager/User
- Implementação SSL/TLS para produção

### 🔧 INFORMAÇÕES TÉCNICAS

| Componente | Detalhes |
|------------|----------|
| **Servidor** | 192.168.156.117 (rede 192.168.156.0/24) |
| **LDAP Server** | 192.168.150.231:389 |
| **Python** | 3.12.3 |
| **PostgreSQL** | 16.11 |
| **Apache** | 2.4.58 |
| **Setuptools** | 67.8.0 (fixo) |
| **Odoo** | 17.0 (oficial) |

---

## CREDENCIAIS

| Sistema | Utilizador | Password |
|---------|-----------|----------|
| PostgreSQL | root | `8kEZ^9I32r&£` |
| Odoo Admin | - | `Admin@PROTOCOLO2026!` |

---

*Documentação criada em: 3 de Março de 2026*
