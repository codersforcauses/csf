import { StorageSerializers, useStorage, type RemovableRef } from '@vueuse/core'

export default <T>(key: string): RemovableRef<T | null> =>
  useStorage(key, null as T | null, undefined, { serializer: StorageSerializers.object })
