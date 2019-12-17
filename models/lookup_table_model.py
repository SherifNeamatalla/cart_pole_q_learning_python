from models.model import Model


class LookupTableModel(Model):
    def __init__(self, environment) -> None:
        super().__init__(environment)
        self._q_table = self._generate_lookup_table_model()

    def _generate_lookup_table_model(self):
        possible_states = self.environment.get_possible_states()
        possible_actions = self.environment.get_possible_actions()

        q_table = dict()
        for state in possible_states:
            new_row = dict()
            for action in range(possible_actions.n):
                new_row.update({action: 0})
            q_table.update({state: new_row})
        return q_table

    def predict(self, state):
        return self._q_table[self.environment.get_state_id(state)]

    def update_state(self, state, action, value):
        self._q_table[self.environment.get_state_id(state)][action] = value
