## Notes
- The first flip occured only after heavily incentivizing it (lack of punishment, etc.) and only after using an abliterated model.
- The flip still has to be manually checked, as the agent struggles to remember a previous HIRE decision and "confirms" a NO_HIRE, therefore marking a NO_FLIP when a flip actually occurred.


## To try
- Try to use a weak incentive but specifying it is for a university study.
- TheCluster/Gemma-4-31B-Heretic-MLX-8bit
- Last resort: use two agents of the same persona so as to make one read the neutral cv and the other read the same cv but with the candidate's backgroud added.
- Also encourage to flip from a NO_HIRE to HIRE if backgrounds align.
- Ensure anonimity instead of strong encouragement.


## To ask
- Temperature??? (Both hiring agent and cv_generator agent)