This is coverage for backend functionality. 
Everything not directly tested here is either for future functionality or implemented in the frontend (by visual confirmation.)
I will provide the frontend routes below to verify.

attendeeHandler.getAttendeeName: not used, for future page personalization.
emailer and mailjet: /emailme except below
	password reset emails not implemented
	
routes.py is the frontend driver, entirely covered by functional frontend testing

main.py missing functions are for cleanup, as it's a bare wrapper over attendeeHandler functionality that is covered.

userHandler: password reset is not implemented, this code would reset passwords in the frontend.

EventHandler:
	getAllEvents: /list-events/userID
	shareEvents: /emailme
	getAllMatching: /index/eventID
	sendTimes: /sendtime/time
	getTimes: /respond/eventID
	getAllDetails: not implemented.