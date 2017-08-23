function login(user, pass){
	var response = document.getElementById("LoginResponse");
	// Check that both fields were filled
	if (user && pass){
		// Check if user exists
		if (profile) {
						
		}
		else {
			// This user does not exist
			response.innerHTML = "That user does not exist."
		}
	}
	else {
		// Alert that fields must be filled
		response.innerHTML = "Please give both a username and a password."
	}
}

function newUser(name) { 
	// Create a new user profile as a player
}
