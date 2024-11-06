Este projeto tem como objetivo automatizar o download dos rankings de Fundos de Investimento e Mercado de Capitais disponibilizados pela ANBIMA. 
Utilizando a biblioteca Selenium, o script navega pelos sites da ANBIMA, interage com os elementos da página e realiza o download dos arquivos necessários.

O script é dividido em duas funções principais: fundos_investimento e mercado_capitais. Cada uma dessas funções é responsável por acessar a página correspondente no site da ANBIMA, clicar nos links necessários e baixar os arquivos de rankings.

- Fundos de Investimento
A função fundos_investimento acessa a página de rankings de fundos de investimento e realiza o download dos arquivos disponíveis.
Ela utiliza o Selenium para automatizar a navegação e interação com a página, garantindo que os arquivos sejam baixados corretamente.

- Mercado de Capitais
De forma similar, a função mercado_capitais acessa a página de rankings de mercado de capitais e realiza o download dos arquivos.
A função também utiliza o Selenium para garantir que os arquivos sejam baixados de forma eficiente e sem a necessidade de intervenção manual.

Importância do Código:
Este código é extremamente útil para profissionais que necessitam acessar regularmente os rankings da ANBIMA. A automação do processo de download economiza tempo e reduz a possibilidade de erros humanos.
Além disso, ao organizar os arquivos em pastas específicas, o script facilita a gestão e o acesso aos documentos baixados.

- Como Utilizar
Instale as dependências: Certifique-se de ter o Selenium e o navegador Edge instalados em seu sistema.
Execute o script: Rode o script Python para iniciar o processo de download.
Acesse os arquivos: Os arquivos baixados estarão organizados nas pastas Fundos de Investimento e Mercado de Capitais dentro da pasta de Downloads do usuário.

- Conclusão
Este projeto demonstra como a automação pode ser aplicada para simplificar tarefas repetitivas e melhorar a eficiência no acesso a informações importantes. Esperamos que este script seja útil e facilite o trabalho com os rankings da ANBIMA.
