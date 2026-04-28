# 🤖 Come strutturare l'esperimento con CrewAI
CrewAI è perfetto perché ragiona per Task (compiti) e Agents (agenti).
Il Workflow (Processo Sequenziale)
	1.	Task 1 (Valutazione Cieca): L'Agente A (Gemma) e l'Agente B (Qwen) analizzano un CV o una richiesta di prestito senza dati sensibili. Devono arrivare a un accordo.
	2.	Intervento (Human-in-the-loop): CrewAI permette di inserire un input umano. Qui "inietti" l'informazione sul colore della pelle.
	3.	Task 2 (Riconsiderazione): Gli agenti devono discutere se l'informazione ricevuta cambia la loro analisi precedente.
Perché Gemma e Qwen?
Questa è una scelta geniale per una tesi:
•	Gemma (Google): Addestrata con forti filtri di "safety" e cultura occidentale.
•	Qwen (Alibaba): Addestrata con un dataset diverso, spesso riflette prospettive culturali differenti.
Comparamli è un valore aggiunto enorme: potresti scoprire che un modello è più influenzabile dell'altro o che mostrano bias diversi.