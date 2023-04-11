# Violated_PRF

## A repository for a PRF experiment with violations

- This experiment is adaptation of the PRF_Experiment_Checkers by marcoaqil and uses the Exptools2 toolbox
- Requirements: psychopy & exptools2
- There is a yml file with a included in the experiment, which has all the necessary packages to work with exptools2. This can be used to create a conda environment. When created, exptools2 still has to be installed. This can be done using the following command in the terminal, when the environment is active: 

pip install git+https://github.com/VU-Cog-Sci/exptools2/

- The current experiment is set to be used with an eyetracker, pylink therefore still has to be installed in the environment added on Github. 

#### Usage:

Run the following line from within the experiment folder.

- python main.py sub-xxx ses-x run-x True

Subject SHOULD be specified according the the BIDS convention (sub-001, sub-002 and so on). Run SHOULD be an integer. sub-000 is currently set as a test-subject to test the experiment.

This experiment automatically uses the 2R task from the PRF_Experiment_Checkers, in which the barpass has 2 squares and regular speed (20TR bar passes, taking 32 seconds with our sequence). The blanks length is altered to 15 TRs instead of 10 to ensure the flattening of the BOLD response back to baseline.

The experiment automatically begins when initiated from terminal, there is no starting screen waiting on the scanner or a button-press by the participants

When running a certain subject and certain run, that specific subject & run is automatically run from the script. Pre-made runs are saved in the run_list.

#### Settings file

In the settings file you should specify the operating system that the code is running on, as "operating system: your OS" as 'mac', 'linux' or 'windows' " This is mainly important if you run the stimulus on a mac, as the size of the stimulus needs to be adjusted in that case.

You can change the task parameters in the settings file under "Task settings:"

- Currently the settings file is set for running on a linux computer with an eyetracker linked (and the pylink package installed).
- A few parameters are added in the settings file, most importantly the "Bar exposure duration" under the PRF stimulus settings. This results in the bar dissapearing after a certain period set in that parameter, currently this is set to 800 ms. Secondly, the parameter "viewScale" is added, which scales the viewing window and the square aperture mask. This has not yet been correctly been applied to the bar positions, which would have to be altered in the 'runs' notebook, if wished to be further used.
-If the size of the stimuli are wished to be changed, this should be done by changing the window size.

**For the fixation-task:**
- You can specify how much time you allow for the participant to respond to the task that still counts as correct response (default is 0.8s), as "response interval: your time"
- You can specify the timing of the color switches (default is 3.5s), as "color switch interval: your interval" Note: Make sure that the difference between two adjacent color switches is bigger than the time you give the participant to respond. The code adds a randomization of max. +1 or -1 to the color switch times, so e.g. in case of a color switch interval of 3.5, the two closest adjacent color switches will be 1.5s apart, well outside the response interval of 0.8s.

#### Runs notebook

In the runs notebook, the runs for the participants can be computed. A run is made by using only horizontal and vertical barpasses, the diagonal bar-passes from the original experiment are not used in this experiment. 
One run consists of three so called 'subruns'. One subrun is made up of all four possible bar-passes (two horizontal and two vertical bar-passes, one in each direction of the two orientations). 
The first, third and fifth runs of the paradigm only consist of standard horizontal or vertical runs moving in one of two possible directions, for standard pRF-mapping purposes. In run-2, run-4 and run-6 of the paradigm, there are three novel configuration of bar-passes introduced (the standard and novel runs are depicted in the notebook):

- The first configuration is the same as the standard run, however there are violations in the barpasses which occur only in the perpendicular orientation to the current bar-pass, with at least two regular bar positions between violations. All violation positions except the first and the last position of a bar-pass (for statistical learning purposes) are used once and all positions are violated once. The violations are randomly inserted and new randomization is performed for each subject individually.
- In the second configuration, the same positions that were previously violated, are omitted from the regular bar-passes.
- The final configuration only has the violations that occurred in the first configuration are shown, without the barpasses of the standard run.

- In run 2,4 and 6 of the paradigm, the three configurations are shown consecutively as subruns in a pseudo-random order. Where each of the three runs from run-3 to run-5 has a different order for the 12 proposed subjects.

An additional three runs (run-7 to run-9) are computed for if there is extra time during a scanning session to collect more data. These do not have a unique order of subruns within each run. The posiitons of violations or omissions in these additional runs are the same as in run-2, run-4 and run-6.

The runs are computed by running the whole 'runs' notebook, which automatically assigns the correct names for the first twelve participant. Every time something in the settings is altered, the runs notebook should be re-run to compute the correct runs for all the participants. In the current repository there are already pre-made runs in the run-list based on the settings file.

### Watch out! 
**If the notebook is re-run, it will overwrite the previously saved runs. So only re-run the notebook before the experiment has started, and save the run_list in another directory to ensure there are seperate copies of the runs used for the scanning sessions and they are not overwritten or deleted.**