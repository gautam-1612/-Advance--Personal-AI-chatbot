import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    chatHistory: [],
    isLoading: false,
    error: null,
}

const chatHistorySlice = createSlice({
    name: "chatHistory",
    initialState,
    reducers: {
        addMessage: (state, action) => { 
            state.chatHistory.push(action.payload);
        },
        changeStatus: (state, action) => {
            state.isLoading = action.payload;
        },
    }
});


export default chatHistorySlice.reducer;
export const {addMessage, changeStatus} = chatHistorySlice.actions;