import {configureStore} from '@reduxjs/toolkit'
import themeReducer from '../slice/theme'
import ChatHistoryReducer from '../slice/chatHistory'

export default configureStore ({
    reducer : {
        theme: themeReducer,
        chatHistory: ChatHistoryReducer
    },
})
