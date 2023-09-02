

class task:
	
	t1 = 1
	fieldmap = 1
	scan = 1
	shortname = ""
	logfile = 1
	t2 = 1
	dti_ap = 1
	dti_pa = 1
	gre_fieldmap = 1
	gre_fieldmap_ph = 1
	
	def __init__(self,name):
		self.name = name

class subject:
	

	observation = task("observation")
	observation.shortname = "OBS"

	disgust = task("disgust")
	disgust.shortname = "DIS"

	sensory_obs = task("sensory_obs")
	sensory_obs.shortname = "SENS_OBS"

	sensory_tactile = task("sensory_tactile")
	sensory_tactile.shortname = "SENS"

	resting = task("resting")

	resting_old = task("resting_old")

	diffusion = task("diffusion")

	def __init__(self,code):
		self.code = code

	def get_scanfile(self,task):

		if task == "observation":
			taskname = "%s-Observation_Task_MB_1.nii.gz" % self.observation.scan
		elif task == "disgust":
			taskname = "%s-Disgust_Task_Long.nii.gz" % self.disgust.scan
		elif task =="sensory_obs":
			taskname = "%s-Observation_Touch_Long.nii.gz" % self.sensory_obs.scan
		elif task =="sensory_tactile":
			taskname = "%s-SensoryTouchAndSound.nii.gz" % self.sensory_tactile.scan
		elif task == "resting":
			taskname = "%s-Resting_State_7min.nii.gz" % self.resting.scan
		elif task == "resting_old":
			taskname = "%s-Resting_State_MB.nii.gz" % self.resting.scan

		return taskname

	def get_dtifile(self,task):

		if task == "diffusion":
			# taskname1 = "%s-DWI_98dir_PA.nii.gz" % self.diffusion.dti_pa
			# taskname2 = "%s-DWI_98dir_AP.nii.gz" % self.diffusion.dti_ap
			# taskname_t2 = "%s-t2w4radiology.nii.gz" % self.diffusion.t2
			# taskname_gre1_old1 = "%s-gre_field_mapping.nii.gz" % self.diffusion.gre_fieldmap_old1
			# taskname_gre1_old2 = "%s-gre_field_mappinga.nii.gz" % self.diffusion.gre_fieldmap_old1
			# taskname_gre2_old = "%s-gre_field_mapping.nii.gz" % self.diffusion.gre_fieldmap_old2
			# taskname_gre1 = "%s-gre_field_mapping_e1.nii.gz" % self.diffusion.gre_fieldmap
			# taskname_gre2 = "%s-gre_field_mapping_e2.nii.gz" % self.diffusion.gre_fieldmap
			# taskname_greph = "%s-gre_field_mapping_ph.nii.gz" % self.diffusion.gre_fieldmap_ph
			# taskname_bval1 = "%s-DWI_98dir_PA.bval" % self.diffusion.dti_pa
			# taskname_bval2 = "%s-DWI_98dir_AP.bval" % self.diffusion.dti_ap
			# taskname_bvec1 = "%s-DWI_98dir_PA.bvec" % self.diffusion.dti_pa
			taskname_bvec2 = "%s-DWI_98dir_AP.bvec" % self.diffusion.dti_ap

		# return taskname1, taskname2, taskname_t2, taskname_gre1, taskname_gre2, taskname_greph, taskname_gre1_old1, taskname_gre1_old2, taskname_gre2_old, taskname_bval1, taskname_bval2, taskname_bvec1, taskname_bvec2
		return taskname_bvec2

	# def get_scanfile_new(self,task):

	# 	if task == "observation":
	# 		taskname = "%s-Observation_Task_MB_1.nii.gz" % self.observation.scan
	# 	elif task == "imitation":
	# 		taskname = "%s-Imitation_Task_MB_2.nii.gz" % self.imitation.scan
	# 	elif task == "execution":
	# 		taskname = "%s-Func_Execution_Task_MB.nii.gz" % self.execution.scan
	# 	elif task == "mentalizing":
	# 		taskname = "%s-Mentalizing_Task_MB_3.nii.gz" % self.mentalizing.scan
	# 	elif task == "resting":
	# 		taskname = "%s-Resting_State_7min.nii.gz" % self.resting.scan

	# 	return taskname

	def get_t1file(self,task):

		if task == "observation":
			t1name = "%s-t1_mprage_short_brain.nii.gz" % self.observation.t1
		elif task == "disgust":
			t1name = "%s-t1_mprage_short_brain.nii.gz" % self.disgust.t1
		elif task == "sensory_obs":
			t1name = "%s-t1_mprage_short_brain.nii.gz" % self.sensory_obs.t1
		elif task == "sensory_tactile":
			t1name = "%s-t1_mprage_short_brain.nii.gz" % self.sensory_tactile.t1
		elif task == "resting":
			t1name = "%s-t1_mprage_short_brain.nii.gz" % self.resting.t1
		elif task == "resting_old":
			t1name = "%s-t1_mprage_short_brain.nii.gz" % self.resting.t1
		
		return t1name
