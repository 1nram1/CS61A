# recursive function  

编写递归函数时，通常在以下情形下你可能需要编写辅助函数（helper functions）：
初始化参数： 当递归函数需要初始化一些参数，这些参数在递归的后续调用中不应该被重置时，你可以在主函数中初始化这些参数，然后递归调用辅助函数。
隐藏实现细节： 如果递归函数的实现涉及复杂逻辑或者需要多个步骤，你可使用辅助函数来隐藏这些复杂性。这样，主递归函数看起来更简洁，更容易理解。
保持接口简洁： 当你想向用户提供一个简洁的函数接口，但是实际的递归逻辑需要更多的参数来跟踪状态时，辅助函数可以用于包装这些复杂性。
累积结果： 如果在递归过程中需要累积结果（比如列表或字符串），你可能需要一个额外的参数来收集这些结果，使用辅助函数可以避免让主递归函数的用户关心这些累积参数。
维护状态： 当递归过程需要维护状态（比如访问的节点标记等），使用辅助函数可以帮助你在多次递归调用中维护这些状态。
分步递归处理： 当问题可以分解为不同的独立递归步骤时，使用多个辅助函数让每一步都清晰地映射到问题的一个子部分，这有助于代码的模块化和复用。
总结，辅助函数是提高递归函数可读性、易用性和模块化的一种重要手段。在设计递归程序时，恰当地使用辅助函数可以极大地提升程序的质量和维护性。