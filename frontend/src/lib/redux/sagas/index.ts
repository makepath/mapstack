// Libraries
import { SagaIterator } from 'redux-saga'
import { all, fork } from 'redux-saga/effects'

// Custom
import layersSagas from 'storage/layers/saga'

export default function* rootSaga(): SagaIterator {
  yield all([fork(layersSagas)])
}
