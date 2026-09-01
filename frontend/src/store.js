import {configureStore} from '@reduxjs/toolkit'
import themeReducer from '../slice/theme'

export default configureStore ({
    reducer : {
        theme: themeReducer,
    },
})