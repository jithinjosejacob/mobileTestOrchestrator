import subprocess 





class IOSOrchestrator:
    IOS_SIMULATOR_START_COMMAND= "open -a simulator" 
    IOS_SIMULATOR_STOP_COMMAND = "xcrun simctl shutdown all"
    NVM_SWITCH_COMMAND = "nvm use 16"
    IOS_WDIO_DIR_PATH="/Users/surajkumar/Documents/GitHub/webdriverio-appium"
    RUN_TESTS_COMMAND="npm run iosApp"
    NVM_INITIALIZER = "source ~/.nvm/nvm.sh"

    def __init__(self) -> None:
        pass
    def __start__ios__simulator__(self):
        print("Starting IOS Simulator....")
        start_ios = subprocess.Popen(IOSOrchestrator.IOS_SIMULATOR_START_COMMAND,shell=True)
        start_ios.wait()
        print("IOS simulator successfully started.")
 
    

    def __stop__ios__simulator__(self):
        print("Shutting down all IOS simulators...")
        stop_ios =subprocess.Popen(IOSOrchestrator.IOS_SIMULATOR_STOP_COMMAND,shell=True)
        stop_ios.wait()
        print("IOS simulators successfully shut down.")

    def execute_tests(self):
        self.__start__ios__simulator__()

        command_for_tests = "{} && {} && cd {} && {}".format(IOSOrchestrator.NVM_INITIALIZER,IOSOrchestrator.NVM_SWITCH_COMMAND,IOSOrchestrator.IOS_WDIO_DIR_PATH,IOSOrchestrator.RUN_TESTS_COMMAND)
        print("starting execution of test cases...")    
        print(command_for_tests)
        test_executor = subprocess.Popen(command_for_tests,shell=True,executable='/bin/zsh')
        exit_code=test_executor.wait()
        print("{} is the exit code for the test process".format(exit_code))
        print("done executing test cases.")
        self.__stop__ios__simulator__()