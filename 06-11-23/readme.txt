socket e stomp

- User: -> genera 10 richieste attendendo 1 sec
	- Invoca il metodo void print(string int)
		I.	pahtFile -> generato in modo casuale /user/file_{num}.{ext}
				num tra 0 e 100, ext tra doc e txt
		II.	tipo (bw/gs/color) generato in modo casuale

- PrintServer: 
	- Interfaccia IPrinter
		- void print(str,str)
			avvia un processo produttore
				- inserisce in una coda 'process-safe' path-tipo
	- Processo consumatore: -> avviato al lancio
		I. 	preleva la stringa e la inserisce in stomp /queue/{tip}

-BW print:
	I.	riceve -> si avvia se da terminale si inserisce bw o gs
	II.	scrive su file bw.txt o gs.txt e stampa a video

-color print:
	I.	riceve -> si avvia se da terminale si inserisce doc o txt
	II.	scrive su file color.txt  e stampa a video


User <-> Printer PROXYSKELETON eredita TCP
Printer <-> bw/color queue stomp
