@ stdcall RtlInitializeConditionVariable(ptr)
@ stdcall RtlWakeConditionVariable(ptr)
@ stdcall RtlWakeAllConditionVariable(ptr)
@ stdcall RtlSleepConditionVariableCS(ptr ptr ptr)
@ stdcall RtlSleepConditionVariableSRW(ptr ptr ptr long)
@ stdcall RtlInitializeSRWLock(ptr)
@ stdcall RtlAcquireSRWLockShared(ptr)
@ stdcall RtlReleaseSRWLockShared(ptr)
@ stdcall RtlAcquireSRWLockExclusive(ptr)
@ stdcall RtlReleaseSRWLockExclusive(ptr)
