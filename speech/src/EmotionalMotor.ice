//******************************************************************
// 
//  Generated by RoboCompDSL
//  
//  File name: EmotionalMotor.ice
//  Source: EmotionalMotor.idsl
//  
//****************************************************************** 
#ifndef ROBOCOMPEMOTIONALMOTOR_ICE
#define ROBOCOMPEMOTIONALMOTOR_ICE
module RoboCompEmotionalMotor
{
	interface EmotionalMotor
	{
		void expressJoy ();
		void expressSadness ();
		void expressSurprise ();
		void expressFear ();
		void expressAnger ();
		void expressDisgust ();
		void expressNeutral ();
		void talking (bool setTalk);
	};
};

#endif
