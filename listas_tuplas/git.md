## Pra que serve o Git?
- sistemas de controle de versões e como eles podem ajudar o nosso fluxo de desenvolvimento

    - Nos ajudam a manter um histórico de alterações;

    - Nos ajudam a ter controle sobre cada alteração no código;

    - Nos ajudam para que uma alteração de determinada pessoa não influencie na alteração realizada por outra;

    - Etc.

- Outros sistemas de controle de versão: CVS, SVN, Mercurial, GIT

- Nos deixa organizar o trabalho em equipe, mantendo as alterações nos arquivos em um servidor específico para isso

- Permite armazenamento e acesso a um histórico de modificações

- Funciona offline

- O git init inicializa um repositório no diretório em que o comando for executado. A partir deste comando, o Git poderá gerenciar as modificações realizadas nos arquivos.

- Execute o comando git status analisa o estado do repositório

- Configurações iniciais:

    - ``git config --local user.name "Seu nome aqui"``

    - ``git config --local user.email "seu@email.aqui"``


- `git status`:

    - HEAD: Estado atual do nosso código, ou seja, onde o Git os colocou

    - Working tree: Local onde os arquivos realmente estão sendo armazenados e editados

    - index: Local onde o Git armazena o que será commitado, ou seja, o local entre a working tree e o repositório Git em si.

- `git log`:
    
    - visualizar o histórico de alterações no projeto

- Nunca devemos ter commits de códigos que não funcionam

- Um commit é a forma de salvar um estado ou versão do nosso código

- `git add`: adiciona arquivos a serem commitados

- Antes de sincronizar as nossas mudanças no código com algum repositório remoto, precisamos antes adicioná-lo ao nosso repositório local --> `git remote add nome-repositorio caminho/para/o/repositorio`

- `git remote add`:  adiciona links para os repositórios remotos

- `git clone`:  baixa um repositório pela primeira vez, clonando-o

- `git push`: envia as nossas alterações para um repositório remoto

- `git pull`: atualiza o nosso repositório com os dados no repositório remoto

- O merge junta os trabalhos e gera um merge commit. O rebase aplica os commits de outra branch na branch atual.

- `git log --graph`: para ver as linhas de desenvolvimento (branches)

- Com o git checkout nós desfazemos uma alteração que ainda não foi adicionada ao index ou stage, ou seja, antes do git add. Depois de adicionar com git add, para desfazer uma alteração, precisamos tirá-la deste estado, com git reset. Agora, se já realizamos o commit, o comando git revert pode nos salvar.

- `git stash`: quando precisamos pausar o desenvolvimento de alguma funcionalidade, ou correção, antes de finalizar, talvez não seja interessante realizar um commit, pois o nosso código pode não estar funcionando ainda

    - para visualizar quais alterações estão na stash, podemos utilizar o comando `git stash list`

    - `git stash apply <numero>`: podemos aplicar uma alteração específica da stash

    - `git stash drop <numero>`: remove determinado item da stash

    - `git stash pop`: aplica e remove a última alteração que foi adicionada na stash

- `git checkout --help`, em uma tradução livre é: "Atualizar os arquivos na working tree para ficarem na versão especificada. [...]". Basicamente, podemos deixar o nosso código no estado do último commit de uma branch, de um commit específico, ou mesmo tags (que veremos adiante).

- `git revert`: gera um novo commit informando que alterações foram desfeitas | reverte as alterações realizadas em um commit

- `git tag -a <nome> <mensagem>`: gera uma nova tag. Cria versões de um projeto

    - `git tag`: visualiza as tags

- `git diff`: vemos as alterações em nossos arquivos que não foram adicionadas para commit (com git add)

    - `git diff <branch1>..<branch2>`: compara as alterações entre duas branches

    - `git diff <commit1>..<commit2>`: compara as alterações feitas entre um commit e outro


http://git-school.github.io/visualizing-git/







