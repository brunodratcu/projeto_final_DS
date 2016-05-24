def verificaemail():
    a=input("digite seu e-mail ")
    if "@" not in a:
        print('''Insira um '@' no endereço de e-mail''')
        verificaemail()
    elif a.count("@")>1:
        print('''Digite um e-mail válido: Com no máximo um '@ - arroba' e tente mais uma vez''')
        verificaemail()
    elif "." not in (a.split("@")[1]):
        print('''Vc não digitou um e-mail compatível com uma classe de domínio - Não usou '.' - Ponto, tente de novo''')
        verificaemail()
    elif ("!" in a) or ("#" in a) or ("%" in a) or (" " in a) or ("&" in a) or ("*" in a) or ("(" in a) or (")" in a) or ("/" in a) or ("|" in a) or ("ç" in a) or ("á" in a) or ("à" in a) or ("ã" in a) or ("â" in a) or ("é" in a) or ("ê" in a) or ("í" in a) or ("õ" in a) or ("ô" in a) or ("ò" in a) or ("ó" in a) or ("ú" in a) or ("è" in a) or ("ù" in a) or ("~" in a) or ("," in a) or (";" in a) or (":" in a) or ("[" in a) or ("]" in a) or ("{" in a) or ("}" in a) or ("^" in a) or ("´" in a) or ("`" in a):
        print("Digite um e-mail sem caracteres especiais")
        verificaemail()
    elif (a[a.index("@")+1])==".":
        print('''Não existe ponto (.) logo depois de arroba (@) em e-mail''' )
        verificaemail()
    elif (a[-1]==".") or (a[-2]==".") or (a[-1]==".") or (int(a[-1])==0) or (int(a[-1])==1) or (int(a[-1])==2) or (int(a[-1])==3) or (int(a[-1])==4) or (int(a[-1])==5) or (int(a[-1])==6) or (int(a[-1])==7) or (int(a[-1])==8) or (int(a[-1])==9) or (int(a[-1])==9) or (a[-2]==".") or (a[-2]==".") or (a[-2]==".") or (int(a[-2])==0) or (int(a[-2])==1) or (int(a[-2])==2) or (int(a[-2])==3) or (int(a[-2])==4) or (int(a[-2])==5) or (int(a[-2])==6) or (int(a[-2])==7) or (int(a[-2])==8) or (int(a[-2])==9) or (int(a[-2])==9) or (a[-3]==".") or (a[-3]==".") or (a[-3]==".") or (int(a[-3])==0) or (int(a[-3])==1) or (int(a[-3])==2) or (int(a[-3])==3) or (int(a[-3])==4) or (int(a[-3])==5) or (int(a[-3])==6) or (int(a[-3])==7) or (int(a[-3])==8) or (int(a[-3])==9) or (int(a[-3])==9):
        print("Insira uma e-mail que pertence à uma classe de domínio válida")
        verificaemail()
    else:
        print("login")
        

verificaemail()
