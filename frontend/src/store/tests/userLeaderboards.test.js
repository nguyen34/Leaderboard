import userLeaderboards from "@/store/modules/userLeaderboards";
import { expect } from "@jest/globals";
import { createStore } from "vuex";

describe("userLeaderboards Store Test", () => {
    let store;
    let mockLeaderboards;
    let mockActions = {
        fetchUsers: jest.fn(),
        addUser: jest.fn(),
        deleteUser: jest.fn(),
        incrementUserScore: jest.fn(),
        decrementUserScore: jest.fn(),
    };
    beforeEach(() => {
        mockLeaderboards = {
            ...userLeaderboards,
            actions: mockActions,
        };
        store = createStore(mockLeaderboards);
        store.state.users = [];
    });

    it("Test Initial Store State", () => {
        expect(store.state.users).toEqual([]);
    });

    it("Test setUsers Mutation", () => {
        const users = [
            {
                id: 1,
                name: "Test User",
                points: 0,
            },
        ];
        store.commit("setUsers", users);
        expect(store.state.users).toEqual(users);
    });

    it("Test addUser Mutation", () => {
        const user = {
            id: 1,
            name: "Test User",
            age: 20,
            address: "Test Address",
            points: 0,
        };
        store.commit("addUser", user);
        expect(store.state.users).toEqual([user]);
    });
    it("Test deleteUser Mutation", () => {
        const user = {
            id: 1,
            name: "Test User",
            age: 20,
            address: "Test Address",
            points: 0,
        };
        store.commit("addUser", user);
        expect(store.state.users).toEqual([user]);
        store.commit("deleteUser", user);
        expect(store.state.users).toEqual([]);
    });
    it("Test incrementUserScore Mutation", () => {
        const user = {
            id: 1,
            name: "Test User",
            age: 20,
            address: "Test Address",
            points: 0,
        };
        store.commit("addUser", user);
        expect(store.state.users).toEqual([user]);
        store.commit("incrementUserScore", user);
        expect(store.state.users[0].points).toEqual(1);
    });
    it("Test decrementUserScore Mutation", () => {
        const user = {
            id: 1,
            name: "Test User",
            age: 20,
            address: "Test Address",
            points: 1,
        };
        store.commit("addUser", user);
        expect(store.state.users).toEqual([user]);
        store.commit("decrementUserScore", user);
        expect(store.state.users[0].points).toEqual(0);

        // Should still be 0 after decrementing again
        store.commit("decrementUserScore", user);
        expect(store.state.users[0].points).toEqual(0);
    });
    // A bit of a formality since the actions are mocked and only function as API calls which are tested on the backend but
    // I wanted to include it for completeness
    it("Test fetchUsers Action", async () => {
        const users = [
            {
                id: 1,
                name: "Test User",
                points: 0,
            },
        ];
        mockActions.fetchUsers.mockResolvedValue(users);
        store.commit("setUsers", users);
        expect(store.state.users).toEqual(users);
    });
    it("Test addUser Action", async () => {
        const user = {
            id: 1,
            name: "Test User",
            age: 20,
            address: "Test Address",
            points: 0,
        };
        mockActions.addUser.mockResolvedValue(user);
        store.commit("addUser", user);
        expect(store.state.users).toEqual([user]);
    }
    );
});