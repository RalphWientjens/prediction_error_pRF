# Violated_PRF

## A repository for a PRF experiment with violations

- This experiment is adaptation of the PRF_Experiment_Checkers by marcoaqil and uses the Exptools2 toolbox
- requirements: psychopy & exptools2

#### Usage:

Run the following line from within the experient folder.

- python main.py sub-xxx ses-x task-2R run-x

Subject SHOULD be specified according the the BIDS convention (sub-001, sub-002 and so on). Run SHOULD be an integer.

This task uses the 2R task from marcoaqil, in which the barpass has 2 squares and regular speed (20TR bar passes, aka 30 seconds with our standard sequence).

Currently, an incomplete run is used as an example violated PRF experiment (see 'runs notebook') when running the experiment, this should still be altered to also directly accessible from initiation of the experiment. This still has to be changed.

#### Settings file

In the settings file you should specify the operating system that the code is running on, as "operating system: your OS" as 'mac', 'linux' or 'windows' This is mainly important if you run the stimulus on a mac, as the size of the stimulus needs to be adjusted in that case.

You can change the task parameters in the settings file under "Task settings:"

- you can specify how much time you allow for the participant to respond that still counts as correct response (default is 0.8s), as "response interval: your time"
- you can specify the timing of the color switches (default is 3.5s), as "color switch interval: your interval" Note: Make sure that the difference between two adjacent color switches is bigger than the time you give the participant to respond. The code adds a randomization of max. +1 or -1 to the color switch times, so e.g. in case of a color switch interval of 3.5, the two closest adjacent color switches will be 1.5s apart, well outside the response interval of 0.8s.
- Currently the settings file is set for ease of editing the experiment and running it on a macbook. For an actual MRI experiment, this should be changed.

#### Runs notebook

In the runs notebook, the runs for the participants can be computed. A standard run is made by using only horizontal and vertical barpasses. The first section of the paradigm only consists of such runs. In second section of the paradigm, there are three different configuration of bar-passes:

- The first configuration is the same as the standard run, however there are violations in the barpasses which occur only in the perpendicular orientation, with at least two regular bar positions between violations. All violation positions except the first and the last position of a bar-pass (due to limited visibility) are used once and all positions are violated once. The violations are randomly inserted and new randomiztion can be made for each subject individually.
- The third configuration only has the violations that occurred in the previous configuration are shown, without the barpasses of the standard run.
- In the final configuration, the same positions that were previously violated, are now omitted from the regular bar-passes.

- In the second section of the paradigm, the three configurations are shown consecutively for each bar-orientation in a random order.

The final, total runs can be made by using either of the two large functions: create_violation_run() and new_run(). Here a name can be given to the total run, which can be subject specific. This run will then be saved in the run_list folder in the experiment folder.
##### **Note! : Now the notebook only saves the violated part of the run, this still has to be altered to all three parts combined. Also: Currently, the window size is hard-coded to [3840, 2160], this still has to be changed if the window size is changed.**