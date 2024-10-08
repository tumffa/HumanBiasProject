from .dialog import Dialog


class SessionManager:
    """Manages sessions

    Attributes:
        sessions: A dictionary of dialog objects
    """

    def __init__(self):
        self.sessions = {}

    def new_session(self, initial_prompt, agents, session_format):
        """Create a new dialog object

        Args:
            initial_prompt (str): The initial prompt for the dialog
            agents (list): A dictionary of agents {"AgentObj": "model"}
        Returns:
            int: The dialog id
            Dialog: The dialog object
        """
        new_id = len(self.sessions)
        session = Dialog(initial_prompt, agents, session_format)
        self.sessions[new_id] = session
        return new_id, session

    def get_session_prompts(self, session_id):
        """Get the prompts for the next round of a dialog object

        Args:
            session_id (int): The id of the dialog object
        Returns:
            list: A list of prompts for the next round
        """
        return self.sessions[session_id].get_prompts()

    def update_session_with_responses(self, session_id, responses):
        """Update a dialog object with responses

        Args:
            session_id (int): The id of the dialog object
            responses (list): A list of responses
        """
        self.sessions[session_id].update_with_responses(responses)

    def get_session(self, session_id):
        print(self.sessions)
        print(session_id)
        return self.sessions[session_id]

    def delete_session(self, session_id):
        del self.sessions[session_id]

    def all_sessions(self):
        # return a dictionary of dialog objects as dictionaries
        dictionary = {k: v.to_dict() for k, v in self.sessions.items()}
        return dictionary

    def get_latest_session_id(self):
        return len(self.sessions) - 1
