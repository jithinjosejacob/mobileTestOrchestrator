import subprocess

class AndroidOrchestrator: 
    DEVICE_NAME="Pixel3"
    EMULATOR_PATH="/Users/jjj/Library/Android/sdk/tools/emulator"
    ANDROID_SIMULATOR_START_COMMAND = "{} -avd {}".format(EMULATOR_PATH,DEVICE_NAME) 
    ANDROID_SIMULATOR_STOP_COMMAND="adb kill-server" 
    NVM_SWITCH_COMMAND = "nvm use 16"
    ANDROID_WDIO_DIR_PATH="/Users/jjj/Desktop/SourceCode/webdriverio"
    RUN_TESTS_COMMAND="npm run androidApp"
    NVM_INITIALIZER = "source ~/.nvm/nvm.sh"


    def __init__(self) -> None:
        pass

    def __start__android__simulator__(self):
        print("Starting Android Simulator....")
        start_android = subprocess.Popen(AndroidOrchestrator.ANDROID_SIMULATOR_START_COMMAND,shell=True)
        start_android.wait()
        print("Android simulator successfully started.")


    def __stop__android__simulator__(self):
        print("Shutting down all Android simulators....")
        stop_android  = subprocess.Popen(AndroidOrchestrator.ANDROID_SIMULATOR_STOP_COMMAND,shell=True)
        stop_android.wait()
        print("Android simulator successfully shut down")
    
    def execute_tests(self):
        self.__start__android__simulator__()
        command_for_tests = "{} && {} && cd {} && {}".format(AndroidOrchestrator.NVM_INITIALIZER,AndroidOrchestrator.NVM_SWITCH_COMMAND,AndroidOrchestrator.ANDROID_WDIO_DIR_PATH,AndroidOrchestrator.RUN_TESTS_COMMAND)
        print("starting execution of test cases...")    
        test_executor = subprocess.Popen(command_for_tests,shell=True,executable='/bin/zsh')
        exit_code=test_executor.wait()
        print("{} is the exit code for the test process".format(exit_code))
        print("done executing test cases.")
        self.__stop__android__simulator__()
