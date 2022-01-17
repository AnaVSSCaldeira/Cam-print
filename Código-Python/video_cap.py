import cv2 as cv #importando a biblioteca OpenCv para realizar a captura da camera

webcam = cv.VideoCapture(0) #capturando a camera
count=0 #contador para tirar print de quantas fotos quisermos
path='insira_seu_caminho_aqui' #caminho para salvar o print tirado

if webcam.isOpened(): #se a webcam abrir
    validacao, frame = webcam.read() #le cada frame da camera, e valida
    while validacao: #se estiver tudo ok
        validacao,frame = webcam.read()
        key=cv.waitKey(50) #tecla que a pessoa digitou
        if key == 27: #se a pessoa teclou 'Esc' o programa acaba
            break
        elif key == 32: #se apertou 'Espaço' tira um print da tela
            #salva o print gerado com o diretorio, nome e contador
            cv.imwrite(str(path)+'Foto_'+str(count)+'.png',frame)
            #coloca um texto apos apertar a tecla para avisar que o print foi tirado
            cv.putText(frame,'Foto tirada!',(50,50),cv.FONT_HERSHEY_SIMPLEX,1,(0, 0, 0),2,cv.LINE_4)
            #aumenta o contador
            count+=1
        #mostra a camera
        cv.imshow('VIDEO',frame)
else: #se a webcam nao abrir
    print('Erro ao abrir a camera!')

webcam.release() #libera a camera
cv.destroyAllWindows() #destroi todas as janelas