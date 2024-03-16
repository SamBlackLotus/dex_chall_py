# Questions and Answers

# MENU

Q. path = "/home/samara/Projects/dex_challenge/data"
Existe alguma forma de puxar isso direto do sistema, para não ficar hardcode?



Q.    monster_path = f"{path}/{monster_category}/{file_format}/{monster_file}"
        
        if os.path.exists(monster_path):
            print(monster_path)
tentei usar o relpath mas ele não valida a existencia do arquivo, só traz um caminho relativo.

Q. Sempre que eu uso um comando no Menu inicial o programa executa até o final e para, como eu faço pra resetar ele e trazer de volta o menu inicial no caso por exemplo do HELP.
