import LeaderBoard from '@/components/LeaderBoard.vue';
import { expect } from '@jest/globals';
import { shallowMount } from '@vue/test-utils';
import { createVuetify } from 'vuetify';
import { createStore } from 'vuex';

describe('LeaderBoard', () => {
    let store;
    let wrapper;
    let vuetify;
    let mockFetchUsers = jest.fn().mockImplementation(() => Promise.resolve());
    let mockDeleteUser = jest.fn().mockImplementation(() => Promise.resolve());
    let mockIncrementUserScore = jest.fn().mockImplementation(() => Promise.resolve());
    let mockDecrementUserScore = jest.fn().mockImplementation(() => Promise.resolve());
    let mockUsers = [
        {
            id: 1,
            name: 'Test User',
            age: 20,
            address: 'Test Address',
            points: 0,
        },
        {
            id: 2,
            name: 'Test User 2',
            age: 20,
            address: 'Test Address 2',
            points: 1,
        },
        {
            id: 3,
            name: 'Test User 3',
            age: 20,
            address: 'Test Address 3',
            points: 2,
        },
        {   
            id: 4,
            name: 'Test User 4',
            age: 20,
            address: 'Test Address 4',
            points: 3,
        }
    ];
    beforeEach(() => {
        vuetify = createVuetify();
        store = createStore({
            modules: {
                userLeaderboards: {
                    namespaced: true,
                    state: {
                        users: mockUsers,
                    },
                    actions: {
                        fetchUsers: mockFetchUsers,
                        deleteUser: mockDeleteUser,
                        incrementUserScore: mockIncrementUserScore,
                        decrementUserScore: mockDecrementUserScore,
                    },
                },
            },
        });
        wrapper = shallowMount(LeaderBoard, {
            global: {
                plugins: [store, vuetify],
            },
        });
    });

    it('renders properly', () => {
        expect(wrapper).toBeTruthy();
        expect(wrapper.vm.showUserDetails).toBe(false);
        expect(wrapper.vm.selectedUser).toEqual(null);
        expect(wrapper.vm.searchFilter).toBe('');
        // This should equal the reverse of mockUsers since it orders by points in descending order by default
        expect(wrapper.vm.displayedUsers).toEqual(mockUsers.reverse());
        expect(wrapper.vm.sortOrder).toBe('desc');
        expect(wrapper.vm.sortHeader).toBe('points');
    });
    it('getUsers should call fetchUsers', async () => {
        await wrapper.vm.getUsers();
        expect(mockFetchUsers).toHaveBeenCalled();
    });
    it('handleDelete should call deleteUser', async () => {
        await wrapper.vm.handleDelete(1);
        expect(mockDeleteUser).toHaveBeenCalled();
    });
    it('handleIncrementScore should call incrementUserScore', async () => {
        const user = {
            id: 1,
            name: 'Test User',
            age: 20,
            address: 'Test Address',
            points: 0,
        };
        await wrapper.vm.handleIncrement(user);
        expect(mockIncrementUserScore).toHaveBeenCalled();
    });
    it('handleDecrementScore should call decrementUserScore', async () => {
        const user = {
            id: 1,
            name: 'Test User',
            age: 20,
            address: 'Test Address',
            points: 0,
        };
        await wrapper.vm.handleDecrement(user);
        expect(mockDecrementUserScore).toHaveBeenCalled();
    });
    it('showUserDetailsDialog should toggle user details dialog', () => { 
        expect(wrapper.vm.showUserDetails).toBe(false);
        expect(wrapper.vm.selectedUser).toEqual(null); 
        const user = {
            id: 1,
            name: 'Test User',
            age: 20,
            address: 'Test Address',
            points: 0,
        };
        wrapper.vm.showUserDetailsDialog(user);
        expect(wrapper.vm.showUserDetails).toBe(true);
        expect(wrapper.vm.selectedUser).toEqual(user);
    });
    it('filterAndSortUsers should filter and sort according to the provided parameters', () => {
        expect(wrapper.vm.displayedUsers).toEqual(mockUsers.reverse());
        wrapper.vm.filterAndSortUsers('name', 'asc');
        expect(wrapper.vm.displayedUsers).toEqual(mockUsers);
        wrapper.vm.filterAndSortUsers('name', 'desc');
        expect(wrapper.vm.displayedUsers).toEqual(mockUsers.reverse());
        wrapper.vm.filterAndSortUsers('points', 'asc');
        expect(wrapper.vm.displayedUsers).toEqual(mockUsers);

        // Now with searchFilter set to something
        wrapper.vm.searchFilter = 'Test User 2';
        wrapper.vm.filterAndSortUsers('name', 'asc');
        expect(wrapper.vm.displayedUsers).toEqual([mockUsers[1]]);
    });
    it('toggleNameSort should change the sortOrder and sortHeader based off its current values', () => {
        expect(wrapper.vm.sortOrder).toBe('desc');
        expect(wrapper.vm.sortHeader).toBe('points');
        wrapper.vm.toggleNameSort();
        expect(wrapper.vm.sortOrder).toBe('asc');
        expect(wrapper.vm.sortHeader).toBe('name');
        wrapper.vm.toggleNameSort();
        expect(wrapper.vm.sortOrder).toBe('desc');
        expect(wrapper.vm.sortHeader).toBe('name');
    });
    it('togglePointsSort should change the sortOrder and sortHeader based off its current values', () => {
        wrapper.vm.sortHeader = 'name';
        expect(wrapper.vm.sortOrder).toBe('desc');
        expect(wrapper.vm.sortHeader).toBe('name');
        wrapper.vm.togglePointSort();
        expect(wrapper.vm.sortOrder).toBe('asc');
        expect(wrapper.vm.sortHeader).toBe('points');
        wrapper.vm.togglePointSort();
        expect(wrapper.vm.sortOrder).toBe('desc');
        expect(wrapper.vm.sortHeader).toBe('points');
    });
    });