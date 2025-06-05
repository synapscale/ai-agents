# API Kiwify - Produtos - Listar Produtos (List Products)




# TEMPLATE PADRÃO PARA DOCUMENTAÇÃO DE APIS


# 1. Cabeçalho e Identificação


| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | `API Kiwify - Produtos - Listar Produtos (List Products)` |
| **Identificador Interno** | `kiwify_prod_001`                   |
| **Título Curto (Ref.)**   | `Kiwify List Products`           |
| **Versão do Documento**   | `1.1.0`                                |
| **Data de Criação**       | `2025-04-11`                                                  |
| **Última Atualização**    | `2025-04-11`                                                  |
| **Autor/Responsável**     | `DocRAGOptimizer`                                    |
| **Fonte Original**        | `https://docs.kiwify.com.br/api-reference/products/list` |
| **URL de Referência**     | `https://docs.kiwify.com.br/api-reference/products/list` |
| **Status do Documento**   | `Em Uso`                              |
| **Ambiente de Referência**| `Produção`                                |
| **Idioma Original**       | `Português (BR)`                                  |
| **Formato de Datas (API)**| `ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)`                       |




*(Ref: Kiwify List Products, ID kiwify_listproducts_001)*
---


## 2. Contexto




> **Resumo:** Esta seção descreve o propósito e o contexto mais amplo do endpoint de listagem de produtos da API Kiwify.




O endpoint `GET /v1/products` da API Kiwify permite que desenvolvedores e sistemas externos recuperem uma lista paginada dos produtos associados a uma conta Kiwify específica. Este endpoint é fundamental para qualquer integração que precise acessar o catálogo de produtos, seja para exibição em interfaces de usuário, sincronização com outros sistemas, ou análise de dados.


Os produtos na plataforma Kiwify representam itens digitais como cursos online, assinaturas (memberships), e-books, entre outros, que podem ser comercializados. O acesso programático a estes produtos facilita a construção de lojas virtuais personalizadas, dashboards administrativos, e integrações com sistemas de ERP, CRM ou Business Intelligence.


Este documento (ID kiwify_prod_001) detalha como autenticar, solicitar, paginar e processar os dados retornados por este endpoint.




*(Ref: Kiwify List Products, ID kiwify_listproducts_001)*
---


## 3. Visão Geral da API/Endpoint(s)




> **Resumo:** Visão de alto nível sobre a funcionalidade e escopo do endpoint de listagem de produtos da Kiwify.




O endpoint `GET /products` permite a recuperação de dados de produtos cadastrados em uma conta Kiwify. Algumas características principais incluem:


* **Paginação**: Os resultados são retornados em páginas, permitindo a navegação eficiente por grandes conjuntos de dados.
* **Dados Detalhados**: Cada produto inclui informações essenciais como identificador único, nome, tipo, status, configurações de pagamento e afiliados.
* **Autenticação Dupla**: Requer tanto um token Bearer padrão quanto um identificador de conta específico.


O endpoint é particularmente útil para:
* Criar catálogos de produtos em sites ou aplicativos
* Monitorar o status e configurações dos produtos
* Realizar auditorias de produtos (ativos vs. inativos) 
* Integrar produtos Kiwify com sistemas externos
* Oferecer funcionalidades de busca e filtro em interfaces personalizadas


A resposta inclui metadados de paginação que facilitam a navegação sequencial por todos os produtos disponíveis.




*(Ref: Kiwify List Products, ID kiwify_listproducts_001)*
---


## 4. Detalhes Técnicos




> **Resumo:** Especificações técnicas detalhadas do endpoint de listagem de produtos, incluindo URL, método HTTP e requisitos de autenticação.




### `Endpoint 1: /products`




*   **Endpoint URL:** `https://public-api.kiwify.com/v1/products`
*   **Método HTTP:** `GET`
*   **Autenticação:** Requer dois headers HTTP:
    *   `Authorization`: Token Bearer OAuth 2.0 - `Bearer {token}` 
    *   `x-kiwify-account-id`: Identificador único da conta Kiwify - `{account_id}`
*   **Content-Type:** `application/json` (resposta)
*   **Versão da API:** `v1`
*   **Protocolo:** `HTTPS` (obrigatório)




*(Ref: Kiwify List Products, ID kiwify_listproducts_001)*
---


## 5. Parâmetros de Entrada




> **Resumo:** Detalhamento de todos os parâmetros que podem ser enviados nas requisições ao endpoint de listagem de produtos.




### `Endpoint 1: /products` (`Query Parameters & Headers`)




| Parâmetro          | Local   | Descrição | Tipo | Obrigatório? | Notas / Exemplo |
| :----------------- | :------ | :-------- | :--- | :----------- | :-------------- |
| `Authorization`    | Header  | Token de acesso OAuth 2.0 para autenticação. Deve ser precedido por "Bearer ". | String | Sim | `Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...` |
| `x-kiwify-account-id` | Header | Identificador único da conta Kiwify à qual os produtos pertencem. | String | Sim | `acc_123456789` |
| `page_size`        | Query   | Define o número de produtos a serem retornados por página. Se omitido, usa o valor padrão da API. | String (Number) | Não | `10`, `50`, `100`. Valor padrão desconhecido. |
| `page_number`      | Query   | Especifica qual página do conjunto de resultados deve ser retornada. Inicia em 1. | String (Number) | Não | `1`, `2`, `3`. Valor padrão presumido: `1`. |




#### Notas Adicionais sobre Parâmetros:


* Os parâmetros de consulta (`page_size` e `page_number`) são opcionais mas fortemente recomendados para controlar a paginação.
* Embora sejam valores numéricos, os parâmetros de consulta devem ser formatados como strings na URL.
* A documentação original não menciona parâmetros adicionais para filtragem (ex: por `status`, `type`, etc.) ou ordenação.




*(Ref: Kiwify List Products, ID kiwify_listproducts_001)*
---


## 6. Parâmetros de Saída (Estrutura da Resposta JSON)




> **Resumo:** Documentação completa da estrutura de dados retornada pelo endpoint de listagem de produtos nas respostas bem-sucedidas.




### `Endpoint 1: /products`




#### 6.1.1 Estrutura Geral




| Campo             | Descrição | Tipo   | Obrigatório? |
| :---------------- | :-------- | :----- | :----------- |
| `pagination`  | Contém metadados sobre a paginação dos resultados. | Objeto | Sim |
| `data`  | Array contendo os objetos de produto da página atual. Pode estar vazio se não houver produtos ou a página estiver além do limite. | Array de Objetos | Sim |




#### 6.1.2 Detalhes do Objeto `pagination`




| Campo Aninhado        | Descrição | Tipo | Obrigatório? | Notas |
| :-------------------- | :-------- | :--- | :----------- | :---- |
| `count` | Número de itens retornados na página atual. | Number | Sim | Pode ser 0 se não houver resultados. |
| `page_number` | Número da página atual retornada. | Number | Sim | Igual ao valor solicitado no parâmetro `page_number`. |
| `page_size` | Número máximo de itens configurado por página. | Number | Sim | Igual ao valor solicitado no parâmetro `page_size` ou valor padrão. |




#### 6.1.3 Detalhes do Objeto `data` (cada item no array)




| Campo Aninhado        | Descrição | Tipo | Obrigatório? | Notas |
| :-------------------- | :-------- | :--- | :----------- | :---- |
| `id` | Identificador único do produto no formato UUID v4. | String | Sim | Ex: `1286a0c0-d492-11ed-9709-c3c5046ec174` |
| `name` | Nome do produto conforme cadastrado na plataforma. | String | Sim | Ex: `Curso de Marketing Digital` |
| `type` | Tipo ou categoria do produto. | String | Sim | Valores possíveis incluem `membership` (assinatura), entre outros. |
| `created_at` | Data e hora de criação do produto no formato ISO 8601 UTC. | String | Sim | Ex: `2023-04-06T15:45:36.013Z` |
| `price` | Preço do produto. | Null ou Number | Sim | Pode ser `null` se o preço não estiver definido ou não for aplicável. |
| `affiliate_enabled` | Indica se o programa de afiliados está habilitado para este produto. | Boolean | Sim | `true` se habilitado, `false` se desabilitado. |
| `status` | Status atual do produto na plataforma. | String | Sim | Valores possíveis incluem `active`, `inactive`, entre outros. |
| `payment_type` | Tipo de pagamento associado ao produto. | String | Sim | Valores possíveis incluem `recurring` (recorrente), `single` (único), entre outros. |




*(Ref: Kiwify List Products, ID kiwify_listproducts_001)*
---


## 7. Exemplos de Requisição e Resposta




> **Resumo:** Exemplos práticos e completos de como construir requisições e interpretar respostas para o endpoint de listagem de produtos.




### `Endpoint 1: /products`




#### 7.1.1 Exemplo de Requisição (cURL)




```bash
curl -X GET "https://public-api.kiwify.com/v1/products?page_size=10&page_number=1" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c" \
  -H "x-kiwify-account-id: acc_123456789" \
  -H "Accept: application/json"
```




#### 7.1.2 Exemplo de Requisição (JavaScript/Fetch)




```javascript
const fetchProducts = async () => {
  try {
    const response = await fetch(
      'https://public-api.kiwify.com/v1/products?page_size=10&page_number=1',
      {
        method: 'GET',
        headers: {
          'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c',
          'x-kiwify-account-id': 'acc_123456789',
          'Accept': 'application/json'
        }
      }
    );
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    
    const data = await response.json();
    console.log(data);
    return data;
  } catch (error) {
    console.error('Error fetching products:', error);
  }
};
```




#### 7.1.3 Exemplo de Resposta (JSON - Sucesso 200 OK)




```json
{
  "pagination": {
    "count": 10,
    "page_number": 1,
    "page_size": 10
  },
  "data": [
    {
      "id": "1286a0c0-d492-11ed-9709-c3c5046ec174",
      "name": "Produto Teste Recorrente",
      "type": "membership",
      "created_at": "2023-04-06T15:45:36.013Z",
      "price": null,
      "affiliate_enabled": false,
      "status": "active",
      "payment_type": "recurring"
    },
    {
      "id": "abcdef12-3456-7890-abcd-ef1234567890",
      "name": "Ebook Completo",
      "type": "ebook",
      "created_at": "2023-05-10T10:20:30.000Z",
      "price": 49.90,
      "affiliate_enabled": true,
      "status": "active",
      "payment_type": "single"
    },
    {
      "id": "98765432-dcba-9876-5432-1fedcba09876",
      "name": "Curso Avançado",
      "type": "course",
      "created_at": "2023-03-15T08:30:00.000Z",
      "price": 299.00,
      "affiliate_enabled": true,
      "status": "active",
      "payment_type": "single"
    }
    // ... mais 7 produtos
  ]
}
```




#### 7.1.4 Exemplo de Resposta (JSON - Erro 401 Unauthorized)




```json
{
  "error": {
    "code": "UNAUTHENTICATED",
    "message": "Authentication required. Provide a valid Bearer token.",
    "request_id": "req_7f8e9d6c5b4a"
  }
}
```




#### 7.1.5 Exemplo de Resposta (JSON - Erro 403 Forbidden)




```json
{
  "error": {
    "code": "FORBIDDEN",
    "message": "You do not have permission to access resources for the specified account ID.",
    "request_id": "req_1a2b3c4d5e6f"
  }
}
```




#### 7.1.6 Exemplo de Resposta (JSON - Última Página/Sem Mais Resultados)




```json
{
  "pagination": {
    "count": 0,
    "page_number": 5,
    "page_size": 10
  },
  "data": []
}
```




*(Ref: Kiwify List Products, ID kiwify_listproducts_001)*
---


## 8. Códigos de Status e Tratamento de Erros




> **Resumo:** Descrição dos códigos de status HTTP retornados pelo endpoint e estratégias para gerenciar erros.




| Status Code               | Descrição Geral                                    | Possível Causa / Ação Recomendada |
| :------------------------ | :------------------------------------------------- | :-------------------------------- |
| `200 OK`                  | Sucesso. A requisição foi processada corretamente e a resposta contém a lista de produtos (potencialmente vazia). | Processar os produtos retornados no array `data`. Implementar navegação para outras páginas conforme necessário. |
| `400 Bad Request`         | Erro na requisição. Parâmetros de consulta inválidos ou mal-formatados. | Verificar se `page_size` e `page_number` são valores numéricos válidos. Corrigir formatação dos parâmetros. |
| `401 Unauthorized`        | Falha na autenticação. Token de acesso inválido, expirado ou ausente. | Renovar o token OAuth. Verificar se o formato do header `Authorization` está correto (`Bearer {token}`). |
| `403 Forbidden`           | Permissão negada. O token é válido, mas não tem permissão para acessar a conta especificada. | Verificar se o `x-kiwify-account-id` está correto e se o usuário autenticado tem acesso a essa conta. |
| `404 Not Found`           | Recurso não encontrado. O endpoint solicitado não existe. | Verificar a URL base e o caminho do endpoint. |
| `429 Too Many Requests`   | Limite de requisições excedido. | Implementar backoff exponencial. Reduzir a frequência das chamadas. Aguardar o tempo indicado no header `Retry-After` (se presente). |
| `500 Internal Server Error`| Erro interno no servidor Kiwify. | Considerar uma nova tentativa após um breve atraso. Se persistir, contatar o suporte da Kiwify. |
| `503 Service Unavailable` | Serviço temporariamente indisponível. | Tentar novamente após o período indicado no header `Retry-After` (se presente) ou após um intervalo razoável. |




### Estratégias para Tratamento de Erros:


1. **Implementar Retentativas com Backoff Exponencial**:
   ```javascript
   async function fetchWithRetry(url, options, maxRetries = 3) {
     let retries = 0;
     while (retries < maxRetries) {
       try {
         const response = await fetch(url, options);
         if (response.status === 429) {
           const retryAfter = response.headers.get('Retry-After') || Math.pow(2, retries);
           await new Promise(resolve => setTimeout(resolve, retryAfter * 1000));
           retries++;
           continue;
         }
         return response;
       } catch (error) {
         if (retries === maxRetries - 1) throw error;
         await new Promise(resolve => setTimeout(resolve, Math.pow(2, retries) * 1000));
         retries++;
       }
     }
   }
   ```


2. **Verificar e Processar o Corpo de Erro**:
   ```javascript
   async function handleErrorResponse(response) {
     const errorData = await response.json();
     console.error(`API Error: ${errorData.error.code} - ${errorData.error.message}`);
     // Log do request_id para troubleshooting
     if (errorData.error.request_id) {
       console.error(`Request ID: ${errorData.error.request_id}`);
     }
     // Ações específicas com base no código de erro
     switch(errorData.error.code) {
       case 'UNAUTHENTICATED':
         // Trigger token refresh
         break;
       case 'FORBIDDEN':
         // Notify user about permissions issue
         break;
       // outros casos
     }
   }
   ```


3. **Monitorar Headers de Limitação de Taxa**:
   ```javascript
   function checkRateLimits(response) {
     const remaining = response.headers.get('X-RateLimit-Remaining');
     const limit = response.headers.get('X-RateLimit-Limit');
     const reset = response.headers.get('X-RateLimit-Reset');
     
     if (remaining && parseInt(remaining) < 10) {
       console.warn(`Rate limit warning: ${remaining}/${limit} requests remaining. Resets at ${new Date(reset * 1000).toISOString()}`);
     }
   }
   ```




*(Ref: Kiwify List Products, ID kiwify_listproducts_001)*
---


## 9. Casos de Uso Comuns (20 Exemplos Específicos)




> **Resumo:** Lista abrangente de 20 casos de uso reais e específicos que demonstram aplicações práticas do endpoint de listagem de produtos.




1.  **Obter a primeira página de produtos com tamanho padrão:**
    *   Objetivo: `Recuperar o primeiro conjunto de produtos usando o tamanho de página padrão.`
    *   Como Fazer: `GET /v1/products`
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


2.  **Listar produtos com tamanho de página personalizado:**
    *   Objetivo: `Controlar precisamente quantos produtos são retornados em cada chamada.`
    *   Como Fazer: `GET /v1/products?page_size=25`
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


3.  **Navegar para uma página específica de resultados:**
    *   Objetivo: `Acessar diretamente uma página particular da lista de produtos.`
    *   Como Fazer: `GET /v1/products?page_size=10&page_number=3` (Acessa a terceira página)
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


4.  **Iterar por todas as páginas de produtos sequencialmente:**
    *   Objetivo: `Recuperar sistematicamente todos os produtos disponíveis na conta.`
    *   Como Fazer: 
    ```javascript
    async function getAllProducts() {
      let allProducts = [];
      let pageNumber = 1;
      const pageSize = 50;
      let hasMorePages = true;
      
      while (hasMorePages) {
        const response = await fetch(`https://public-api.kiwify.com/v1/products?page_size=${pageSize}&page_number=${pageNumber}`, {
          headers: {
            'Authorization': 'Bearer YOUR_TOKEN',
            'x-kiwify-account-id': 'YOUR_ACCOUNT_ID'
          }
        });
        
        const data = await response.json();
        allProducts = [...allProducts, ...data.data];
        
        // Verificar se chegamos à última página
        if (data.data.length === 0 || data.data.length < pageSize) {
          hasMorePages = false;
        } else {
          pageNumber++;
        }
      }
      
      return allProducts;
    }
    ```
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


5.  **Verificar rapidamente se existem produtos na conta:**
    *   Objetivo: `Determinar se há algum produto cadastrado na conta, sem necessidade de processar muitos registros.`
    *   Como Fazer: `GET /v1/products?page_size=1` - Se a resposta tiver `pagination.count === 0`, não há produtos.
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


6.  **Construir um menu dropdown de seleção de produtos:**
    *   Objetivo: `Obter dados básicos para popular uma interface de seleção de produtos.`
    *   Como Fazer: 
    ```javascript
    async function populateProductDropdown(dropdownElement) {
      const response = await fetch('https://public-api.kiwify.com/v1/products?page_size=100', {
        headers: { /* seus headers */ }
      });
      
      const data = await response.json();
      
      // Mapear apenas ID e Nome para o dropdown
      data.data.forEach(product => {
        const option = document.createElement('option');
        option.value = product.id;
        option.textContent = product.name;
        dropdownElement.appendChild(option);
      });
    }
    ```
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


7.  **Sincronizar produtos com um sistema de ERP externo:**
    *   Objetivo: `Manter um sistema externo atualizado com os produtos da Kiwify.`
    *   Como Fazer: 
    ```javascript
    async function syncProductsWithERP() {
      const kiwifyProducts = await getAllProducts(); // função do caso de uso #4
      
      for (const product of kiwifyProducts) {
        // Verificar se o produto já existe no ERP
        const erpProduct = await checkProductInERP(product.id);
        
        if (erpProduct) {
          // Atualizar produto existente
          await updateERPProduct(product.id, {
            name: product.name,
            status: product.status,
            price: product.price,
            productType: product.type,
            lastUpdate: new Date().toISOString()
          });
        } else {
          // Criar novo produto no ERP
          await createERPProduct({
            externalId: product.id,
            name: product.name,
            status: product.status,
            price: product.price,
            productType: product.type,
            createdAt: product.created_at
          });
        }
      }
      
      console.log(`Sincronização concluída: ${kiwifyProducts.length} produtos processados.`);
    }
    ```
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


8.  **Gerar um relatório de produtos ativos vs. inativos:**
    *   Objetivo: `Analisar a distribuição de status dos produtos para fins gerenciais.`
    *   Como Fazer: 
    ```javascript
    async function generateStatusReport() {
      const allProducts = await getAllProducts(); // função do caso de uso #4
      
      const statusCounts = allProducts.reduce((acc, product) => {
        acc[product.status] = (acc[product.status] || 0) + 1;
        return acc;
      }, {});
      
      console.log("Relatório de Status dos Produtos:");
      Object.entries(statusCounts).forEach(([status, count]) => {
        console.log(`${status}: ${count} produtos (${(count/allProducts.length*100).toFixed(1)}%)`);
      });
      
      return statusCounts;
    }
    ```
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


9.  **Exibir um catálogo paginado de produtos em um site:**
    *   Objetivo: `Mostrar produtos para visitantes com navegação por páginas.`
    *   Como Fazer: 
    ```javascript
    // Frontend (React)
    function ProductCatalog() {
      const [products, setProducts] = useState([]);
      const [currentPage, setCurrentPage] = useState(1);
      const [pageSize] = useState(12);
      const [loading, setLoading] = useState(false);
      
      useEffect(() => {
        async function fetchPage() {
          setLoading(true);
          try {
            const response = await fetch(`/api/proxy-products?page=${currentPage}&page_size=${pageSize}`);
            const data = await response.json();
            setProducts(data.data);
          } catch (error) {
            console.error('Error fetching products:', error);
          } finally {
            setLoading(false);
          }
        }
        
        fetchPage();
      }, [currentPage, pageSize]);
      
      return (
        <div className="catalog">
          {loading ? <LoadingSpinner /> : (
            <>
              <div className="product-grid">
                {products.map(product => (
                  <ProductCard 
                    key={product.id}
                    name={product.name}
                    price={product.price}
                    type={product.type}
                  />
                ))}
              </div>
              <Pagination 
                currentPage={currentPage}
                onPageChange={setCurrentPage}
                hasMore={products.length === pageSize}
              />
            </>
          )}
        </div>
      );
    }
    
    // Backend (proxy para evitar exposição de credenciais no frontend)
    app.get('/api/proxy-products', async (req, res) => {
      try {
        const { page = 1, page_size = 12 } = req.query;
        
        const response = await fetch(
          `https://public-api.kiwify.com/v1/products?page_number=${page}&page_size=${page_size}`,
          {
            headers: {
              'Authorization': `Bearer ${process.env.KIWIFY_TOKEN}`,
              'x-kiwify-account-id': process.env.KIWIFY_ACCOUNT_ID
            }
          }
        );
        
        const data = await response.json();
        res.json(data);
      } catch (error) {
        res.status(500).json({ error: 'Failed to fetch products' });
      }
    });
    ```
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


10. **Mostrar produtos recentemente adicionados:**
    *   Objetivo: `Exibir os produtos mais recentes com base na data de criação.`
    *   Como Fazer: `GET /v1/products?page_size=5&page_number=1` e ordenar localmente pelo campo `created_at` (assumindo que a API retorna em ordem cronológica inversa, ou fazer ordenação no cliente).
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


11. **Identificar produtos com afiliados habilitados:**
    *   Objetivo: `Encontrar todos os produtos que permitem programa de afiliados.`
    *   Como Fazer: Buscar todos os produtos e filtrar localmente onde `affiliate_enabled === true`.
    ```javascript
    async function getProductsWithAffiliates() {
      const allProducts = await getAllProducts();
      return allProducts.filter(product => product.affiliate_enabled === true);
    }
    ```
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


12. **Categorizar produtos por tipo:**
    *   Objetivo: `Agrupar produtos de acordo com seu tipo para análise ou exibição.`
    *   Como Fazer: 
    ```javascript
    async function categorizeProductsByType() {
      const allProducts = await getAllProducts();
      
      const productsByType = allProducts.reduce((acc, product) => {
        if (!acc[product.type]) {
          acc[product.type] = [];
        }
        acc[product.type].push(product);
        return acc;
      }, {});
      
      // Exemplo de uso: exibir contagem por tipo
      Object.entries(productsByType).forEach(([type, products]) => {
        console.log(`${type}: ${products.length} produtos`);
      });
      
      return productsByType;
    }
    ```
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


13. **Monitorar novos produtos adicionados desde a última verificação:**
    *   Objetivo: `Identificar produtos criados após uma data específica (ex: última sincronização).`
    *   Como Fazer: 
    ```javascript
    async function getNewProductsSince(lastCheckDate) {
      const allProducts = await getAllProducts();
      const lastCheckTimestamp = new Date(lastCheckDate).getTime();
      
      return allProducts.filter(product => {
        const productTimestamp = new Date(product.created_at).getTime();
        return productTimestamp > lastCheckTimestamp;
      });
    }
    
    // Uso:
    const newProducts = await getNewProductsSince('2023-10-01T00:00:00Z');
    console.log(`${newProducts.length} produtos novos desde a última verificação.`);
    ```
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


14. **Listar produtos com pagamento recorrente:**
    *   Objetivo: `Identificar todos os produtos configurados como assinaturas/pagamentos recorrentes.`
    *   Como Fazer: 
    ```javascript
    async function getRecurringProducts() {
      const allProducts = await getAllProducts();
      return allProducts.filter(product => product.payment_type === 'recurring');
    }
    ```
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


15. **Validar a configuração de autenticação da API:**
    *   Objetivo: `Testar se as credenciais e configuração estão corretas antes de implementar integrações mais complexas.`
    *   Como Fazer: 
    ```javascript
    async function validateApiCredentials() {
      try {
        const response = await fetch('https://public-api.kiwify.com/v1/products?page_size=1', {
          headers: {
            'Authorization': `Bearer ${apiToken}`,
            'x-kiwify-account-id': accountId
          }
        });
        
        if (response.ok) {
          console.log('✅ API credentials are valid');
          return true;
        } else {
          const errorData = await response.json();
          console.error('❌ API validation failed:', errorData.error);
          return false;
        }
      } catch (error) {
        console.error('❌ API validation error:', error.message);
        return false;
      }
    }
    ```
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


16. **Criar um sistema de cache para produtos:**
    *   Objetivo: `Reduzir o número de chamadas à API armazenando resultados temporariamente.`
    *   Como Fazer: 
    ```javascript
    // Implementação simples de cache com tempo de expiração
    class ProductCache {
      constructor(ttlSeconds = 300) { // 5 minutos de TTL padrão
        this.cache = {};
        this.ttlSeconds = ttlSeconds;
      }
      
      async getProducts(page = 1, pageSize = 10) {
        const cacheKey = `products_${page}_${pageSize}`;
        
        // Verificar se temos cache válido
        if (this.cache[cacheKey] && this.cache[cacheKey].expiry > Date.now()) {
          console.log('Cache hit for', cacheKey);
          return this.cache[cacheKey].data;
        }
        
        // Cache miss ou expirado, buscar da API
        console.log('Cache miss for', cacheKey);
        const response = await fetch(
          `https://public-api.kiwify.com/v1/products?page_number=${page}&page_size=${pageSize}`,
          { headers: { /* seus headers */ } }
        );
        
        const data = await response.json();
        
        // Armazenar no cache
        this.cache[cacheKey] = {
          data,
          expiry: Date.now() + (this.ttlSeconds * 1000)
        };
        
        return data;
      }
      
      invalidateCache() {
        this.cache = {};
      }
    }
    
    // Uso:
    const productCache = new ProductCache();
    const firstPageData = await productCache.getProducts(1, 20);
    ```
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


17. **Calcular o valor total do catálogo de produtos:**
    *   Objetivo: `Determinar o valor total de todos os produtos com preço definido.`
    *   Como Fazer: 
    ```javascript
    async function calculateCatalogValue() {
      const allProducts = await getAllProducts();
      
      let totalValue = 0;
      let productsWithPrice = 0;
      let productsWithoutPrice = 0;
      
      allProducts.forEach(product => {
        if (product.price !== null) {
          totalValue += product.price;
          productsWithPrice++;
        } else {
          productsWithoutPrice++;
        }
      });
      
      return {
        totalValue: totalValue.toFixed(2),
        productsWithPrice,
        productsWithoutPrice,
        averagePrice: productsWithPrice > 0 ? (totalValue / productsWithPrice).toFixed(2) : 0
      };
    }
    ```
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


18. **Exportar lista de produtos para CSV:**
    *   Objetivo: `Gerar um arquivo CSV contendo os dados dos produtos para análise externa.`
    *   Como Fazer: 
    ```javascript
    async function exportProductsToCsv() {
      const allProducts = await getAllProducts();
      
      // Definir cabeçalhos
      const headers = [
        'ID', 'Nome', 'Tipo', 'Data de Criação', 
        'Preço', 'Afiliados Habilitados', 'Status', 'Tipo de Pagamento'
      ];
      
      // Mapear produtos para linhas
      const rows = allProducts.map(product => [
        product.id,
        product.name,
        product.type,
        product.created_at,
        product.price !== null ? product.price : 'N/A',
        product.affiliate_enabled ? 'Sim' : 'Não',
        product.status,
        product.payment_type
      ]);
      
      // Combinar cabeçalhos e linhas
      const csvContent = [
        headers.join(','),
        ...rows.map(row => row.join(','))
      ].join('\n');
      
      // No browser, criar um download
      if (typeof window !== 'undefined') {
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.setAttribute('href', url);
        link.setAttribute('download', `kiwify_products_${new Date().toISOString().slice(0, 10)}.csv`);
        link.style.visibility = 'hidden';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      }
      
      return csvContent;
    }
    ```
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


19. **Construir um dashboard de produtos:**
    *   Objetivo: `Apresentar estatísticas e visualizações sobre o catálogo de produtos.`
    *   Como Fazer: `Carregar todos os produtos e calcular métricas como distribuição por tipo, status, média de preços, etc.`
    ```javascript
    async function buildProductDashboardData() {
      const allProducts = await getAllProducts();
      
      // Estatísticas básicas
      const stats = {
        totalProducts: allProducts.length,
        activeProducts: allProducts.filter(p => p.status === 'active').length,
        productsWithAffiliates: allProducts.filter(p => p.affiliate_enabled).length,
        
        // Distribuição por tipo
        productsByType: allProducts.reduce((acc, p) => {
          acc[p.type] = (acc[p.type] || 0) + 1;
          return acc;
        }, {}),
        
        // Distribuição por tipo de pagamento
        productsByPaymentType: allProducts.reduce((acc, p) => {
          acc[p.payment_type] = (acc[p.payment_type] || 0) + 1;
          return acc;
        }, {}),
        
        // Produtos mais recentes (top 5)
        recentProducts: allProducts
          .sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
          .slice(0, 5)
          .map(p => ({ id: p.id, name: p.name, created_at: p.created_at }))
      };
      
      return stats;
    }
    ```
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*


20. **Verificar consistência de dados entre páginas:**
    *   Objetivo: `Garantir que não há duplicação de produtos ao iterar por múltiplas páginas.`
    *   Como Fazer: 
    ```javascript
    async function verifyPaginationConsistency() {
      const pageSize = 10;
      const maxPages = 5; // para testes, limite a um número razoável de páginas
      
      let allProductIds = new Set();
      let duplicates = [];
      
      for (let page = 1; page <= maxPages; page++) {
        const response = await fetch(
          `https://public-api.kiwify.com/v1/products?page_number=${page}&page_size=${pageSize}`,
          { headers: { /* seus headers */ } }
        );
        
        const data = await response.json();
        
        // Se não há mais resultados, interromper o loop
        if (data.data.length === 0) break;
        
        // Verificar cada produto da página
        data.data.forEach(product => {
          if (allProductIds.has(product.id)) {
            duplicates.push({
              id: product.id,
              name: product.name,
              page
            });
          } else {
            allProductIds.add(product.id);
          }
        });
      }
      
      if (duplicates.length > 0) {
        console.warn('⚠️ Encontrados produtos duplicados entre páginas:', duplicates);
      } else {
        console.log('✅ Nenhum produto duplicado encontrado entre páginas.');
      }
      
      return {
        uniqueProductCount: allProductIds.size,
        duplicates
      };
    }
    ```
    *(Ref: Kiwify List Products, ID kiwify_listproducts_001)*




*(Ref: Kiwify List Products, ID kiwify_listproducts_001)*
---


## 10. Notas Adicionais




> **Resumo:** Informações complementares importantes sobre aspectos operacionais, limitações e considerações específicas do endpoint de listagem de produtos.




*   **Paginação e Performance**: 
    * O endpoint utiliza paginação baseada em número de página (`page_number`) e tamanho da página (`page_size`). 
    * Para obter um grande volume de produtos, recomenda-se aumentar o `page_size` (valores como 50-100) para reduzir o número total de requisições, equilibrando com o tempo de resposta.
    * A API não fornece um contador total de produtos em todas as páginas, apenas o número na página atual (`pagination.count`).
    * O fim da paginação é indicado quando a resposta retorna um array `data` vazio ou com menos itens que o `page_size` solicitado.


*   **Filtragem e Ordenação**:
    * A documentação original não menciona suporte a parâmetros de query para filtragem ou ordenação dos resultados. Portanto, qualquer filtragem específica (por status, tipo, etc.) deve ser implementada no lado do cliente após receber os dados.
    * A ordem de retorno dos produtos não está documentada, mas provavelmente segue um padrão como data de criação (mais recentes primeiro) ou alfabético por nome.


*   **Consistência e Cache**:
    * Considerando que produtos não mudam com alta frequência, é recomendável implementar um sistema de cache no lado do cliente para reduzir o número de chamadas à API, especialmente para listagens que serão exibidas em interfaces de usuário.
    * Um TTL (Time To Live) de 5-15 minutos para o cache geralmente é adequado para dados de produtos, dependendo da frequência de atualizações no seu caso específico.


*   **Identifiers e Dados**:
    * O campo `id` retornado para cada produto é um UUID v4 e deve ser tratado como opaco (não dependente de estrutura específica).
    * O campo `price` pode ser `null` em produtos sem preço definido ou em casos especiais (ex: produtos com preços variáveis).
    * O tipo de produto (`type`) pode incluir valores como `membership`, `ebook`, `course`, entre outros. A documentação original não lista todos os valores possíveis.


*   **Limites e Considerações**:
    * Não há informações documentadas sobre limites de taxa (rate limits) para este endpoint.
    * No entanto, é boa prática implementar retries com backoff exponencial para lidar com possíveis erros 429 (Too Many Requests) ou falhas temporárias.
    * O tamanho máximo da página (`page_size`) não é mencionado, mas valores muito altos (>100) podem resultar em tempos de resposta prolongados ou erros.


*   **Práticas Recomendadas**:
    * Para sistemas que precisam de sincronização completa, considere usar um job em background que itera por todas as páginas em intervalos regulares (ex: diariamente), em vez de fazer isso durante interações do usuário.
    * Ao exibir produtos para usuários finais, aplique qualquer filtro relevante (ex: `status === 'active'`) para mostrar apenas produtos disponíveis.
    * Considere implementar mecanismos de revalidação de cache quando operações de criação/edição de produtos são realizadas, para garantir consistência de dados.




*(Ref: Kiwify List Products, ID kiwify_listproducts_001)*
---


## 11. Metadados Internos (Para Indexação e RAG)




> **Resumo:** Metadados estruturados em formato JSON para facilitar a indexação e recuperação por sistemas RAG.




```json
{
  "doc_id": "kiwify_prod_001",
  "api_provider": "Kiwify",
  "api_product_area": "Produtos",
  "endpoint_focus": ["Listar Produtos", "Obter Produtos Paginados", "Recuperar Catálogo"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "Confidential",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Baixa",
  "key_entities_handled": ["Produto", "Paginação", "Catálogo", "Membership", "Curso"],
  "context_level": ["foundational", "intermediate"],
  "topic_cluster": ["e-commerce", "gestão de produtos", "catálogo digital", "api kiwify", "produtos digitais"],
  "db_relations": {
    "tables": ["products", "accounts", "product_types"],
    "schemas": ["public"]
  },
  "related_concepts": [
    "catálogo de produtos", 
    "paginação api", 
    "autenticação bearer", 
    "api rest", 
    "produtos digitais",
    "afiliados kiwify",
    "membership",
    "cursos online",
    "e-commerce digital"
  ],
  "question_embeddings": [
    "Como listar meus produtos na Kiwify via API?",
    "Qual endpoint da Kiwify retorna a lista de produtos?",
    "Como paginar a lista de produtos da Kiwify?",
    "Quais parâmetros são necessários para listar produtos na Kiwify?",
    "Qual a estrutura da resposta ao listar produtos Kiwify?",
    "Como obter o ID de todos os meus produtos Kiwify?",
    "A API da Kiwify permite filtrar produtos por status ou tipo?",
    "Como saber quantos produtos tenho na Kiwify pela API?",
    "Quais campos são retornados para cada produto na API Kiwify?",
    "Como identificar produtos com afiliados habilitados via API?"
  ],
  "reasoning_pathways": ["sequential (pagination)", "retrieval", "filtering (client-side)", "data aggregation"],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Standard",
  "authentication_requirements": ["Bearer Token", "x-kiwify-account-id Header"],
  "typical_integration_points": [
    "Website Frontend", 
    "ERP System", 
    "CRM System", 
    "BI Tools", 
    "Admin Dashboards",
    "Mobile Apps",
    "Analytics Platforms"
  ],
  "common_error_patterns": [
    "authentication_failure (401)", 
    "permission_denied (403)", 
    "invalid_pagination_params (400)",
    "connection_timeout",
    "rate_limit_exceeded"
  ]
}
```




*(Ref: Kiwify List Products, ID kiwify_listproducts_001)*
---


## 12. Checklist de Implementação (Opcional)




> **Resumo:** Lista verificável dos aspectos técnicos a serem considerados na implementação da integração com o endpoint de listagem de produtos.




- [ ] **Configuração Inicial**
  - [ ] Obter credenciais de API da Kiwify (OAuth token)
  - [ ] Configurar armazenamento seguro para o token e account_id
  - [ ] Definir ambiente de destino (produção/sandbox)


- [ ] **Autenticação**
  - [ ] Implementar mecanismo para obtenção do token Bearer
  - [ ] Configurar renovação automática do token expirado (se aplicável)
  - [ ] Armazenar o x-kiwify-account-id de forma segura
  - [ ] Validar a autenticação com uma chamada de teste


- [ ] **Requisição Base**
  - [ ] Configurar URL base da API Kiwify
  - [ ] Implementar configuração de headers HTTP
  - [ ] Validar formato de parâmetros de query string


- [ ] **Paginação**
  - [ ] Implementar mecanismo para definir tamanho da página (page_size)
  - [ ] Criar função para incrementar número da página (page_number)
  - [ ] Desenvolver lógica para detectar a última página
  - [ ] Implementar verificações para evitar loop infinito


- [ ] **Mapeamento de Dados**
  - [ ] Definir modelo/interface para objeto Produto
  - [ ] Criar função de mapeamento do JSON para modelo interno
  - [ ] Implementar validação de campos obrigatórios
  - [ ] Tratar campos potencialmente nulos ou indefinidos


- [ ] **Tratamento de Erros**
  - [ ] Implementar handlers para códigos de status HTTP comuns (400, 401, 403, 404)
  - [ ] Configurar tratamento para erros de rede/timeout
  - [ ] Implementar retry com backoff exponencial para erros 429 e 5xx
  - [ ] Criar sistema de log para rastreamento de erros


- [ ] **Otimização de Performance**
  - [ ] Implementar sistema de cache para reduzir chamadas repetidas
  - [ ] Configurar invalidação de cache apropriada
  - [ ] Definir TTL (Time To Live) adequado para dados em cache
  - [ ] Ajustar tamanho de página para equilibrar latência vs. número de chamadas


- [ ] **Interface de Usuário (se aplicável)**
  - [ ] Criar componentes para exibição de lista de produtos
  - [ ] Implementar controles de paginação na UI
  - [ ] Adicionar indicadores de carregamento durante requisições
  - [ ] Desenvolver formatação adequada para campos (preço, datas)


- [ ] **Testes**
  - [ ] Criar testes unitários para mapeamento de dados
  - [ ] Implementar testes de integração com API real
  - [ ] Testar cenários de erro (timeout, falha de rede, auth inválida)
  - [ ] Validar comportamento com diferentes volumes de dados


- [ ] **Documentação**
  - [ ] Documentar uso da integração para outros desenvolvedores
  - [ ] Criar exemplos de código para casos de uso comuns
  - [ ] Documentar processo de obtenção/renovação de credenciais
  - [ ] Mapear códigos de erro e possíveis soluções




*(Ref: Kiwify List Products, ID kiwify_listproducts_001)*
---


## 13. Glossário de Termos Técnicos




> **Resumo:** Definições claras e concisas dos principais termos técnicos utilizados nesta documentação.




| Termo                     | Definição                                                    |
| :------------------------ | :----------------------------------------------------------- |
| `API (Application Programming Interface)` | Conjunto de definições e protocolos para construir e integrar software de aplicações, permitindo que sistemas diferentes se comuniquem. |
| `Endpoint` | URL específica em uma API que representa um recurso ou ação específica que pode ser acessada por clientes. No caso, `/v1/products` para listar produtos. |
| `REST (Representational State Transfer)` | Estilo de arquitetura para sistemas distribuídos que utiliza HTTP para comunicação e é amplamente utilizado em APIs web. |
| `OAuth 2.0` | Protocolo padrão de autorização que permite que aplicações terceiras obtenham acesso limitado a um serviço em nome do usuário. |
| `Bearer Token` | Tipo de token de acesso que concede acesso ao portador ("bearer") independentemente de sua identidade. Utilizado no header `Authorization`. |
| `Paginação` | Técnica para dividir grandes conjuntos de dados em partes menores (páginas) para otimizar a transferência e processamento. |
| `JSON (JavaScript Object Notation)` | Formato leve de intercâmbio de dados baseado em texto, fácil de ler e escrever por humanos e máquinas. |
| `UUID (Universally Unique Identifier)` | Identificador de 128 bits padronizado, usado para identificar informações em sistemas distribuídos sem coordenação central. |
| `HTTP (Hypertext Transfer Protocol)` | Protocolo de aplicação para sistemas de informação distribuídos, colaborativos e hipermídia, base da comunicação na World Wide Web. |
| `Método GET` | Método HTTP usado para solicitar dados de um recurso específico, sem alterá-lo. |
| `Query String` | Parte de uma URL que contém dados a serem passados para aplicações web, formatada como pares chave-valor após um `?`. |
| `Header HTTP` | Parte de uma requisição ou resposta HTTP que passa informações adicionais entre cliente e servidor. |
| `Status Code HTTP` | Código numérico padronizado retornado por servidores web para indicar o resultado de uma requisição HTTP. |
| `ISO 8601` | Padrão internacional para representação de datas e horas (ex: `2023-04-06T15:45:36.013Z`). |
| `Rate Limit` | Restrição do número de requisições que um cliente pode fazer a uma API em um período específico. |
| `Retry` | Técnica de repetir automaticamente uma operação que falhou, geralmente com intervalo crescente entre tentativas. |
| `Backoff Exponencial` | Algoritmo que aumenta exponencialmente o tempo de espera entre tentativas repetidas. |
| `Middleware` | Software que atua como ponte entre um sistema operacional ou banco de dados e aplicações, especialmente em redes. |
| `TTL (Time To Live)` | Mecanismo que limita o tempo de vida ou idade de dados em cache ou sistemas de computador. |
| `Webhook` | Mecanismo que permite que uma aplicação forneça informações em tempo real para outras aplicações quando ocorrem eventos específicos. |




*(Ref: Kiwify List Products, ID kiwify_listproducts_001)*
---


## 14. Observações Finais sobre Formatação




> **Resumo:** Diretrizes de formatação para garantir a consistência e adequação do documento para sistemas RAG.




*   Use headings (`#`, `##`, `###`) para estruturar hierarquicamente o documento.
*   Use tabelas Markdown para apresentar dados estruturados e comparativos.
*   Use blocos de código (``` ```) com indicação de linguagem para exemplos de código e JSON.
*   Mantenha linguagem clara, objetiva e tecnicamente precisa.
*   Formate nomes de parâmetros, campos e valores de exemplo com backticks (`exemplo`).
*   **Crucial:** Inclua `(Ref: [TITULO_CURTO], ID [ID_INTERNO])` no final de **CADA SEÇÃO PRINCIPAL (##)** e opcionalmente em subitens/chunks.
*   Mantenha os resumos de seção concisos (1-2 linhas) e informativos.
*   Use listas e bullets para informações sequenciais ou enumeradas.
*   Evite abreviações não explicadas ou jargão não definido no documento.
*   Para maior rastreabilidade, considere adicionar a referência também em subseções importantes e casos de uso individuais.




*(Ref: Kiwify List Products, ID kiwify_listproducts_001)*