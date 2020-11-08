from dqn import *
from agent_compiler import combine_agents

def test_agent(env, agent):
    agent.is_test = True
    state = env.reset()
    done = False
    score = 0
    while not done:
        # env.render()
        action = agent.select_action(state)
        next_state, reward, done = agent.step(action)

        state = next_state
        score += reward
    print("test score for agent : ", score)

if __name__ == "__main__":
    # environment
    env = gym.make("CartPole-v0")

    NO_OF_TRAINERS = 50

    agents = [DQNAgent(env) for i in range(NO_OF_TRAINERS)]

    for (i, agent) in enumerate(agents):
        # training loop
        agent.train(2000)

        # Testing
        print('Testing agent ', i)
        test_agent(env, agent)

    main_agent = combine_agents(env, agents)

    print('Testing main_agent')
    test_agent(env, main_agent)

    env.close()