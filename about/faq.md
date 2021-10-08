# 常见问题
[原文链接](https://web.mit.edu/music21/doc/about/faq.html)

## 一般问题
### 我如何提出一个问题，使它在这里收录
Don't you hate FAQs that are not based on anything anyone's ever asked? 要提问，请发送至[https://groups.google.com/g/music21list](https://groups.google.com/g/music21list)。但是请务必先阅读本文中已有的常见问题。

### 为什么叫music21？
todo

### music21的原生数据格式是什么？
简要回答：没有，但没关系。

详细回答：music21是一套用于处理和分析你已有或生成的音乐数据的工具箱。因此，它的优势在于它（以及Python）所具有的，处理许多常用文件格式，以及轻松地扩展以支持更多文件格式的能力。你会发现，大多数时候你需要将数据保存为可交换的格式。并且，由于music21的高自由度，我们不可能开发出一种适用于所有应用场景的文件格式。我们也在工作中使用music21，从未需要过这样一种文件格式。

但如果你必须储存你的music21数据，以下是一些建议：

- 对于可以快速并准确重建的数据，把生成该数据的脚本作为数据存储。
- 如需存储音乐符号，musicXML可满足大多数情况。如需存储音频或乐谱图像，可以使用MIDI或Lilupond->PNG
- 对于不能简单地重建的数据（因为重建的成本太高，依赖用户输入，或者随机生成），可以使用Python的pickle包存储数据。所存储的文件不一定能被高版本的music21读入，所以不应用于长期储存。Run setupSerializationScaffold() and teardownSerializationScaffold() before running pickle.dump(yourStream) and after running pickle.load(yourStream) respectively and almost everything will be preserved.
- 对于不能简单地重建，但又要长期储存或分享的数据，可将你需要的部分保存为XML、json或CSV。参见plistlib[https://docs.python.org/dev/library/plistlib.html](https://docs.python.org/dev/library/plistlib.html)或[https://code.activestate.com/recipes/440595](https://code.activestate.com/recipes/440595)。如果存储完整的python数据结构有困难，可以仅存储难以重建的部分，这样简单一些。Music21对用JSON存储Stream提供了一定的支持，但不完善。
- 如果你需要存储的数据结构太复杂，不能用以上方法存储，那么你应该有足够的经验自己创建一个数据格式。请考虑将你的解决方案贡献到music21以帮助我们改进。

### 用music21可以合成新的声音吗？
是，也不是。music21处理符号音乐而不是音频波型。但是，符号音乐数据可用于很多音频合成包。所以，你可以用music21对象调用其他合成包来合成。

### music21可以直接从图片或pdf读入乐谱吗？
抱歉，这超出了music21的能力范围。这个技术叫OMR（Optical Music Recognition，光学乐谱识别），是一个完整的，独立的研究领域。Audiveris是一个开源的OMR套件，其开发团队已经在开发商业软件SmartScore的过程中获得了经验。music21有一套模块用于优化OMR的输出结果，参见[music21.omr.correctors](https://web.mit.edu/music21/doc/moduleReference/moduleOmrCorrectors.html#moduleomrcorrectors)

### 我想尝试music21，如何安装？
[用户指南，第1章：安装与上手music21](../userguide/1.ipynb)

### 我用的是GNU/Linux或者Unix系统，在配置music21时遇到困难，你们能提供帮助吗？
不幸的是，由于开源操作系统的碎片化，开发团队只能为Mac和Windows用户提供免费帮助（但是提供付费支持，看下面）

### music21缺少一些我需要的特性，如何让music21加入这一特性？
可以向music21的mailing list（或者直接向我们）发邮件，我们会考虑的。但是，我们有一个优先级列表，主要考虑我们认为大多数用户所需要的功能，以及我们自己的研究所需要的功能。如果你希望你的需求立即得到实现，最好的方法是捐助我们，来让我们雇佣更多写代码的学生。

## 咨询
### 不，你不理解，我**真的**需要这个特性！
如果你真的需要music21实现某个功能，我们提供付费支持，按照标准咨询费用收费。请联系cuthbert@mit.edu获得详情与费率。
todo

## 第三方工具
### MusicXML是什么？
MusicXML是在不同软件间交换乐谱的文件格式，例如，music和Finale（或者music21和Sibelius，或Dorico，或Musescore）。它由Recordare（Michael Good, CEO）发明，现在由W3C管理。关于Music21XML的更多信息，请前往：
- [https://www.musicxml.com/](https://www.musicxml.com/)