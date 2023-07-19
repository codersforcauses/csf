import { StorageSerializers, useStorage, type RemovableRef } from "@vueuse/core";

export default <T>(key: string): RemovableRef<T> => useStorage(key, null as T | null, undefined, {serializer: StorageSerializers.object})