from transitions import Machine

#状態の定義
states = ['1', '2', '3']

#遷移の定義
# trigger：遷移関数、source：変化前の状態、dest：変化後の状態
# before：遷移前に実施されるコールバック、after：遷移後に実施されるコールバック
transitions = [
    { 'trigger': 'one_to_two', 'source': '1', 'dest': '2'},
    { 'trigger': 'two_to_three', 'source': '2', 'dest': '3', 'before': 'action_2to3'},
    { 'trigger': 'three_to_one', 'source': '3', 'dest': '1', 'after': 'action_3to1'}
]

#状態を管理したいオブジェクトの元となるクラス
# 遷移時やイベント発生時のアクションがある場合は、当クラスのmethodに記載する
class Matter(object):
    def action_2to3(self):
        print("2 to 3")

    def action_3to1(self):
        print("action_complete")

model = Matter()
machine = Machine(model=model, states=states, transitions=transitions, initial='1', auto_transitions=False)

print(model.state)
model.one_to_two()
print(model.state)
