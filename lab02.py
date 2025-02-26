print("Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda a algumas poucas perguntas para ter uma recomendação.") 
print("Seu SO anterior era Linux?")
print("(0) Não")
print("(1) Sim")
so_linux = input()
if so_linux == "0":
    print("Seu SO anterior era um MacOS?")
    print("(0) Não")
    print("(1) Sim")
    so_macos = input()
    if so_macos == "0":
        print("Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro.")
    elif so_macos == "1":
        print("Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: ElementaryOS, ApricityOS.")
    else:
        print("Opção inválida, recomece o questionário.")



elif so_linux == "1":
    print("É programador/ desenvolvedor ou de áreas semelhantes?")
    print("(0) Não")
    print("(1) Sim")
    print("(2) Sim, realizo testes e invasão de sistemas")
    programador = input()
    if programador == "0":
        print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Ubuntu Mint, Fedora.")
    elif programador == "1":
        print("Gostaria de algo pronto para uso ao invés de ficar configurando o SO?")
        print("(0) Não")
        print("(1) Sim")
        algo_pronto = input()
        if algo_pronto == "0":
            print("Já utilizou Arch Linux?")
            print("(0) Não")
            print("(1) Sim")
            arch_linux = input()
            if arch_linux == "0":
                print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Antergos, Arch Linux.")
            elif arch_linux == "1":
                print("Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Gentoo, CentOS, Slackware.")
            else:
                print("Opção inválida, recomece o questionário.")
        elif algo_pronto == "1":
            print("Já utilizou Debian ou Ubuntu?")
            print("(0) Não")
            print("(1) Sim")
            debian_ubuntu = input()
            if debian_ubuntu == "0":
                print ("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu.")
            elif debian_ubuntu == "1":
                print("Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Manjaro, ApricityOS.")
            else:
                print("Opção inválida, recomece o questionário.")
        else:
            print("Opção inválida, recomece o questionário.")
    elif programador == "2":
        print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Kali Linux, Black Arch.")
    else:
        print("Opção inválida, recomece o questionário.")


    

else:
    print("Opção inválida, recomece o questionário.")