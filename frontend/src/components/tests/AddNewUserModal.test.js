import AddNewUserModal from '@/components/AddNewUserModal';
import { mount } from '@vue/test-utils';

describe('AddNewUserModal', () => {
    let wrapper;
    beforeEach(() => {
        wrapper = mount(AddNewUserModal);
    });

    it('renders properly', () => {
        expect(wrapper).toBeTruthy();
    })
});