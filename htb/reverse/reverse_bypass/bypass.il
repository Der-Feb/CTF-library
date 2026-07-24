.assembly extern mscorlib
{
  .ver 4:0:0:0
  .publickeytoken = (B7 7A 5C 56 19 34 E0 89 ) // .z\V.4..
}
.assembly 'HTBChallange'
{
  .custom instance void class [mscorlib]System.Runtime.Versioning.TargetFrameworkAttribute::'.ctor'(string) =  (
		01 00 1C 2E 4E 45 54 46 72 61 6D 65 77 6F 72 6B   // ....NETFramework
		2C 56 65 72 73 69 6F 6E 3D 76 34 2E 35 2E 32 01   // ,Version=v4.5.2.
		00 54 0E 14 46 72 61 6D 65 77 6F 72 6B 44 69 73   // .T..FrameworkDis
		70 6C 61 79 4E 61 6D 65 14 2E 4E 45 54 20 46 72   // playName..NET Fr
		61 6D 65 77 6F 72 6B 20 34 2E 35 2E 32          ) // amework 4.5.2

  .custom instance void class [mscorlib]System.Reflection.AssemblyTrademarkAttribute::'.ctor'(string) =  (01 00 00 00 00 ) // .....

  .custom instance void class [mscorlib]System.Reflection.AssemblyDescriptionAttribute::'.ctor'(string) =  (01 00 00 00 00 ) // .....

  .custom instance void class [mscorlib]System.Runtime.InteropServices.ComVisibleAttribute::'.ctor'(bool) =  (01 00 00 00 00 ) // .....

  .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilationRelaxationsAttribute::'.ctor'(int32) =  (01 00 08 00 00 00 00 00 ) // ........

  .custom instance void class [mscorlib]System.Reflection.AssemblyCompanyAttribute::'.ctor'(string) =  (01 00 00 00 00 ) // .....

  .custom instance void class [mscorlib]System.Reflection.AssemblyConfigurationAttribute::'.ctor'(string) =  (01 00 00 00 00 ) // .....

  .custom instance void class [mscorlib]System.Reflection.AssemblyProductAttribute::'.ctor'(string) =  (
		01 00 0C 48 54 42 43 68 61 6C 6C 61 6E 67 65 00   // ...HTBChallange.
		00                                              ) // .

  .custom instance void class [mscorlib]System.Reflection.AssemblyCopyrightAttribute::'.ctor'(string) =  (
		01 00 12 43 6F 70 79 72 69 67 68 74 20 C2 A9 20   // ...Copyright .. 
		20 32 30 31 39 00 00                            ) //  2019..

  .custom instance void class [mscorlib]System.Runtime.CompilerServices.RuntimeCompatibilityAttribute::'.ctor'() =  (
		01 00 01 00 54 02 16 57 72 61 70 4E 6F 6E 45 78   // ....T..WrapNonEx
		63 65 70 74 69 6F 6E 54 68 72 6F 77 73 01       ) // ceptionThrows.

  .custom instance void class [mscorlib]System.Runtime.InteropServices.GuidAttribute::'.ctor'(string) =  (
		01 00 24 35 30 38 39 32 32 36 66 2D 31 32 62 36   // ..$5089226f-12b6
		2D 34 30 35 30 2D 39 63 65 33 2D 66 37 63 34 33   // -4050-9ce3-f7c43
		37 32 31 61 35 61 32 00 00                      ) // 721a5a2..

  .custom instance void class [mscorlib]System.Reflection.AssemblyFileVersionAttribute::'.ctor'(string) =  (01 00 07 31 2E 30 2E 30 2E 30 00 00 ) // ...1.0.0.0..

  .custom instance void class [mscorlib]System.Reflection.AssemblyTitleAttribute::'.ctor'(string) =  (
		01 00 0C 48 54 42 43 68 61 6C 6C 61 6E 67 65 00   // ...HTBChallange.
		00                                              ) // .

  .hash algorithm 0x00008004
  .ver  1:0:0:0
}
.mresource private '0'
{
}
.module HTBChallange.exe // GUID = {4B13835A-6F14-4740-B5E0-426A4B735535}


    // method line 1
    .method privatescope static specialname rtspecialname 
           default void '.cctor' ()  cil managed 
    {
        // Method begins at RVA 0x2050
	// Code size 6 (0x6)
	.maxstack 8
	IL_0000:  call void class '5'::'0'()
	IL_0005:  ret 
    } // end of global method .cctor

  .class public auto ansi beforefieldinit '0'
  	extends [mscorlib]System.Object
  {
    .field  public static  string '0'
    .field  public static  string '1'
    .field  public static  string '2'

    // method line 2
    .method public static hidebysig 
           default void '0' ()  cil managed 
    {
        // Method begins at RVA 0x2058
	.entrypoint
	// Code size 42 (0x2a)
	.maxstack 1
	.locals init (
		bool	V_0,
		bool	V_1)
	IL_0000:  nop 
	IL_0001:  call bool class '0'::'1'()
	IL_0006:  stloc.0 
	IL_0007:  ldloc.0 
	IL_0008:  stloc.1 
	IL_0009:  ldloc.1 
	IL_000a:  brfalse.s IL_0016

	IL_000c:  nop 
	IL_000d:  call void class '0'::'2'()
	IL_0012:  nop 
	IL_0013:  nop 
	IL_0014:  br.s IL_0029

	IL_0016:  nop 
	IL_0017:  ldsfld string '5'::'0'
	IL_001c:  call void class [mscorlib]System.Console::WriteLine(string)
	IL_0021:  nop 
	IL_0022:  call void class '0'::'0'()
	IL_0027:  nop 
	IL_0028:  nop 
	IL_0029:  ret 
    } // end of method 0::0

    // method line 3
    .method public static hidebysig 
           default bool '1' ()  cil managed 
    {
        // Method begins at RVA 0x2090
	// Code size 41 (0x29)
	.maxstack 1
	.locals init (
		string	V_0,
		string	V_1,
		bool	V_2)
	IL_0000:  nop 
	IL_0001:  ldsfld string '5'::'1'
	IL_0006:  call void class [mscorlib]System.Console::Write(string)
	IL_000b:  nop 
	IL_000c:  call string class [mscorlib]System.Console::ReadLine()
	IL_0011:  stloc.0 
	IL_0012:  ldsfld string '5'::'2'
	IL_0017:  call void class [mscorlib]System.Console::Write(string)
	IL_001c:  nop 
	IL_001d:  call string class [mscorlib]System.Console::ReadLine()
	IL_0022:  stloc.1 
	IL_0023:  ldc.i4.0 
	IL_0024:  stloc.2 
	IL_0025:  br.s IL_0027

	IL_0027:  ldloc.2 
	IL_0028:  ret 
    } // end of method 0::1

    // method line 4
    .method public static hidebysig 
           default void '2' ()  cil managed 
    {
        // Method begins at RVA 0x20c8
	// Code size 85 (0x55)
	.maxstack 3
	.locals init (
		string	V_0,
		string	V_1,
		bool	V_2)
	IL_0000:  nop 
	IL_0001:  ldsfld string '5'::'3'
	IL_0006:  stloc.0 
	IL_0007:  ldsfld string '5'::'4'
	IL_000c:  call void class [mscorlib]System.Console::Write(string)
	IL_0011:  nop 
	IL_0012:  call string class [mscorlib]System.Console::ReadLine()
	IL_0017:  stloc.1 
	IL_0018:  ldloc.0 
	IL_0019:  ldloc.1 
	IL_001a:  call bool string::op_Equality(string, string)
	IL_001f:  stloc.2 
	IL_0020:  ldloc.2 
	IL_0021:  brfalse.s IL_0041

	IL_0023:  nop 
	IL_0024:  ldsfld string '5'::'5'
	IL_0029:  ldsfld string '0'::'2'
	IL_002e:  ldsfld string '5'::'6'
	IL_0033:  call string string::Concat(string, string, string)
	IL_0038:  call void class [mscorlib]System.Console::Write(string)
	IL_003d:  nop 
	IL_003e:  nop 
	IL_003f:  br.s IL_0054

	IL_0041:  nop 
	IL_0042:  ldsfld string '5'::'7'
	IL_0047:  call void class [mscorlib]System.Console::WriteLine(string)
	IL_004c:  nop 
	IL_004d:  call void class '0'::'2'()
	IL_0052:  nop 
	IL_0053:  nop 
	IL_0054:  ret 
    } // end of method 0::2

    // method line 5
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x2129
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void object::'.ctor'()
	IL_0006:  nop 
	IL_0007:  ret 
    } // end of method 0::.ctor

    // method line 6
    .method private static hidebysig specialname rtspecialname 
           default void '.cctor' ()  cil managed 
    {
        // Method begins at RVA 0x2132
	// Code size 11 (0xb)
	.maxstack 8
	IL_0000:  ldsfld string '5'::'8'
	IL_0005:  stsfld string '0'::'2'
	IL_000a:  ret 
    } // end of method 0::.cctor

  } // end of class 0

  .class public auto ansi '1'
  	extends [mscorlib]System.Attribute
  {
    .custom instance void class [mscorlib]System.AttributeUsageAttribute::'.ctor'(valuetype [mscorlib]System.AttributeTargets) =  (01 00 05 00 00 00 00 00 ) // ........

    .field  public  string '0'

    // method line 7
    .method public specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x213e
	// Code size 20 (0x14)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void object::'.ctor'()
	IL_0006:  nop 
	IL_0007:  ldarg.0 
	IL_0008:  ldsfld string '5'::'9'
	IL_000d:  stfld string '1'::'0'
	IL_0012:  nop 
	IL_0013:  ret 
    } // end of method 1::.ctor

  } // end of class 1

  .class public auto ansi '2'
  	extends [mscorlib]System.Attribute
  {
    .custom instance void class [mscorlib]System.AttributeUsageAttribute::'.ctor'(valuetype [mscorlib]System.AttributeTargets) =  (01 00 05 00 00 00 00 00 ) // ........

    .field  public  string '0'

    // method line 8
    .method public specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x2153
	// Code size 20 (0x14)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void object::'.ctor'()
	IL_0006:  nop 
	IL_0007:  ldarg.0 
	IL_0008:  ldsfld string '5'::a
	IL_000d:  stfld string '2'::'0'
	IL_0012:  nop 
	IL_0013:  ret 
    } // end of method 2::.ctor

  } // end of class 2

  .class public auto ansi '3'
  	extends [mscorlib]System.Attribute
  {
    .custom instance void class [mscorlib]System.AttributeUsageAttribute::'.ctor'(valuetype [mscorlib]System.AttributeTargets) =  (01 00 05 00 00 00 00 00 ) // ........

    .field  public  string '0'

    // method line 9
    .method public specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x2168
	// Code size 20 (0x14)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void object::'.ctor'()
	IL_0006:  nop 
	IL_0007:  ldarg.0 
	IL_0008:  ldsfld string '5'::b
	IL_000d:  stfld string '3'::'0'
	IL_0012:  nop 
	IL_0013:  ret 
    } // end of method 3::.ctor

  } // end of class 3

  .class public auto ansi '4'
  	extends [mscorlib]System.Attribute
  {
    .custom instance void class [mscorlib]System.AttributeUsageAttribute::'.ctor'(valuetype [mscorlib]System.AttributeTargets) =  (01 00 05 00 00 00 00 00 ) // ........

    .field  public  string '0'

    // method line 10
    .method public specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x217d
	// Code size 20 (0x14)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void object::'.ctor'()
	IL_0006:  nop 
	IL_0007:  ldarg.0 
	IL_0008:  ldsfld string '5'::c
	IL_000d:  stfld string '4'::'0'
	IL_0012:  nop 
	IL_0013:  ret 
    } // end of method 4::.ctor

  } // end of class 4

  .class private auto ansi abstract sealed '5'
  	extends [mscorlib]System.Object
  {
    .field  assembly static  string '0'
    .field  assembly static  string '1'
    .field  assembly static  string '2'
    .field  assembly static  string '3'
    .field  assembly static  string '4'
    .field  assembly static  string '5'
    .field  assembly static  string '6'
    .field  assembly static  string '7'
    .field  assembly static  string '8'
    .field  assembly static  string '9'
    .field  assembly static  string a
    .field  assembly static  string b
    .field  assembly static  string c

    // method line 11
    .method public static 
           default void '0' ()  cil managed 
    {
        // Method begins at RVA 0x2194
	// Code size 170 (0xaa)
	.maxstack 2
	IL_0000:  call class [mscorlib]System.Reflection.Assembly class [mscorlib]System.Reflection.Assembly::GetExecutingAssembly()
	IL_0005:  ldstr "0"
	IL_000a:  callvirt instance class [mscorlib]System.IO.Stream class [mscorlib]System.Reflection.Assembly::GetManifestResourceStream(string)
	IL_000f:  call unsigned int8[] class '7'::'3'(class [mscorlib]System.IO.Stream)
	IL_0014:  newobj instance void class '6'::'.ctor'(unsigned int8[])
	IL_0019:  dup 
	IL_001a:  call instance string class '6'::'6'()
	IL_001f:  stsfld string '5'::'0'
	IL_0024:  dup 
	IL_0025:  call instance string class '6'::'6'()
	IL_002a:  stsfld string '5'::'1'
	IL_002f:  dup 
	IL_0030:  call instance string class '6'::'6'()
	IL_0035:  stsfld string '5'::'2'
	IL_003a:  dup 
	IL_003b:  call instance string class '6'::'6'()
	IL_0040:  stsfld string '5'::'3'
	IL_0045:  dup 
	IL_0046:  call instance string class '6'::'6'()
	IL_004b:  stsfld string '5'::'4'
	IL_0050:  dup 
	IL_0051:  call instance string class '6'::'6'()
	IL_0056:  stsfld string '5'::'5'
	IL_005b:  dup 
	IL_005c:  call instance string class '6'::'6'()
	IL_0061:  stsfld string '5'::'6'
	IL_0066:  dup 
	IL_0067:  call instance string class '6'::'6'()
	IL_006c:  stsfld string '5'::'7'
	IL_0071:  dup 
	IL_0072:  call instance string class '6'::'6'()
	IL_0077:  stsfld string '5'::'8'
	IL_007c:  dup 
	IL_007d:  call instance string class '6'::'6'()
	IL_0082:  stsfld string '5'::'9'
	IL_0087:  dup 
	IL_0088:  call instance string class '6'::'6'()
	IL_008d:  stsfld string '5'::a
	IL_0092:  dup 
	IL_0093:  call instance string class '6'::'6'()
	IL_0098:  stsfld string '5'::b
	IL_009d:  dup 
	IL_009e:  call instance string class '6'::'6'()
	IL_00a3:  stsfld string '5'::c
	IL_00a8:  pop 
	IL_00a9:  ret 
    } // end of method 5::0

  } // end of class 5

  .class private auto ansi beforefieldinit '6'
  	extends [mscorlib]System.Object
  {
    .field  private initonly  class [mscorlib]System.IO.BinaryReader '0'

    // method line 12
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' (class [mscorlib]System.IO.Stream '0')  cil managed 
    {
        // Method begins at RVA 0x224a
	// Code size 24 (0x18)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void object::'.ctor'()
	IL_0006:  ldarg.0 
	IL_0007:  ldarg.1 
	IL_0008:  call class [mscorlib]System.Text.Encoding class [mscorlib]System.Text.Encoding::get_Unicode()
	IL_000d:  newobj instance void class [mscorlib]System.IO.BinaryReader::'.ctor'(class [mscorlib]System.IO.Stream, class [mscorlib]System.Text.Encoding)
	IL_0012:  stfld class [mscorlib]System.IO.BinaryReader '6'::'0'
	IL_0017:  ret 
    } // end of method 6::.ctor

    // method line 13
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' (unsigned int8[] '0')  cil managed 
    {
        // Method begins at RVA 0x2263
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  newobj instance void class [mscorlib]System.IO.MemoryStream::'.ctor'(unsigned int8[])
	IL_0007:  call instance void class '6'::'.ctor'(class [mscorlib]System.IO.Stream)
	IL_000c:  ret 
    } // end of method 6::.ctor

    // method line 14
    .method public hidebysig 
           instance default string '6' ()  cil managed 
    {
        // Method begins at RVA 0x2271
	// Code size 12 (0xc)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld class [mscorlib]System.IO.BinaryReader '6'::'0'
	IL_0006:  callvirt instance string class [mscorlib]System.IO.BinaryReader::ReadString()
	IL_000b:  ret 
    } // end of method 6::6

    // method line 15
    .method public hidebysig 
           instance default int8 '7' ()  cil managed 
    {
        // Method begins at RVA 0x227e
	// Code size 12 (0xc)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld class [mscorlib]System.IO.BinaryReader '6'::'0'
	IL_0006:  callvirt instance int8 class [mscorlib]System.IO.BinaryReader::ReadSByte()
	IL_000b:  ret 
    } // end of method 6::7

    // method line 16
    .method public hidebysig 
           instance default int32 '8' ()  cil managed 
    {
        // Method begins at RVA 0x228b
	// Code size 12 (0xc)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld class [mscorlib]System.IO.BinaryReader '6'::'0'
	IL_0006:  callvirt instance int32 class [mscorlib]System.IO.BinaryReader::ReadInt32()
	IL_000b:  ret 
    } // end of method 6::8

    // method line 17
    .method public hidebysig 
           instance default int64 '9' ()  cil managed 
    {
        // Method begins at RVA 0x2298
	// Code size 12 (0xc)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld class [mscorlib]System.IO.BinaryReader '6'::'0'
	IL_0006:  callvirt instance int64 class [mscorlib]System.IO.BinaryReader::ReadInt64()
	IL_000b:  ret 
    } // end of method 6::9

    // method line 18
    .method public hidebysig 
           instance default float32 a ()  cil managed 
    {
        // Method begins at RVA 0x22a5
	// Code size 12 (0xc)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld class [mscorlib]System.IO.BinaryReader '6'::'0'
	IL_0006:  callvirt instance float32 class [mscorlib]System.IO.BinaryReader::ReadSingle()
	IL_000b:  ret 
    } // end of method 6::a

    // method line 19
    .method public hidebysig 
           instance default float64 b ()  cil managed 
    {
        // Method begins at RVA 0x22b2
	// Code size 12 (0xc)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld class [mscorlib]System.IO.BinaryReader '6'::'0'
	IL_0006:  callvirt instance float64 class [mscorlib]System.IO.BinaryReader::ReadDouble()
	IL_000b:  ret 
    } // end of method 6::b

  } // end of class 6

  .class public auto ansi abstract sealed beforefieldinit '7'
  	extends [mscorlib]System.Object
  {
    .field public static literal  int32 '0' = not found

    // method line 20
    .method public static hidebysig 
           default unsigned int8[] '2' (unsigned int8[] '0')  cil managed 
    {
        // Method begins at RVA 0x22c0
	// Code size 205 (0xcd)
	.maxstack 4
	.locals init (
		class [mscorlib]System.Security.Cryptography.RijndaelManaged	V_0,
		class [mscorlib]System.IO.MemoryStream	V_1,
		unsigned int8[]	V_2,
		unsigned int8[]	V_3,
		class [mscorlib]System.Security.Cryptography.ICryptoTransform	V_4,
		class [mscorlib]System.Security.Cryptography.CryptoStream	V_5,
		unsigned int8[]	V_6,
		unsigned int8[]	V_7)
	IL_0000:  newobj instance void class [mscorlib]System.Security.Cryptography.RijndaelManaged::'.ctor'()
	IL_0005:  stloc.0 
	.try { // 3
	  IL_0006:  ldloc.0 
	  IL_0007:  ldc.i4 128
	  IL_000c:  callvirt instance void class [mscorlib]System.Security.Cryptography.SymmetricAlgorithm::set_BlockSize(int32)
	  IL_0011:  ldloc.0 
	  IL_0012:  ldc.i4.1 
	  IL_0013:  callvirt instance void class [mscorlib]System.Security.Cryptography.SymmetricAlgorithm::set_Mode(valuetype [mscorlib]System.Security.Cryptography.CipherMode)
	  IL_0018:  ldloc.0 
	  IL_0019:  callvirt instance void class [mscorlib]System.Security.Cryptography.SymmetricAlgorithm::GenerateKey()
	  IL_001e:  ldloc.0 
	  IL_001f:  callvirt instance void class [mscorlib]System.Security.Cryptography.SymmetricAlgorithm::GenerateIV()
	  IL_0024:  ldarg.0 
	  IL_0025:  newobj instance void class [mscorlib]System.IO.MemoryStream::'.ctor'(unsigned int8[])
	  IL_002a:  stloc.1 
	  .try { // 2
	    IL_002b:  ldloc.0 
	    IL_002c:  callvirt instance unsigned int8[] class [mscorlib]System.Security.Cryptography.SymmetricAlgorithm::get_Key()
	    IL_0031:  ldlen 
	    IL_0032:  conv.i4 
	    IL_0033:  newarr [mscorlib]System.Byte
	    IL_0038:  stloc.2 
	    IL_0039:  ldloc.0 
	    IL_003a:  callvirt instance unsigned int8[] class [mscorlib]System.Security.Cryptography.SymmetricAlgorithm::get_IV()
	    IL_003f:  ldlen 
	    IL_0040:  conv.i4 
	    IL_0041:  newarr [mscorlib]System.Byte
	    IL_0046:  stloc.3 
	    IL_0047:  ldloc.1 
	    IL_0048:  ldloc.2 
	    IL_0049:  ldc.i4.0 
	    IL_004a:  ldloc.2 
	    IL_004b:  ldlen 
	    IL_004c:  conv.i4 
	    IL_004d:  callvirt instance int32 class [mscorlib]System.IO.Stream::Read(unsigned int8[], int32, int32)
	    IL_0052:  pop 
	    IL_0053:  ldloc.1 
	    IL_0054:  ldloc.3 
	    IL_0055:  ldc.i4.0 
	    IL_0056:  ldloc.3 
	    IL_0057:  ldlen 
	    IL_0058:  conv.i4 
	    IL_0059:  callvirt instance int32 class [mscorlib]System.IO.Stream::Read(unsigned int8[], int32, int32)
	    IL_005e:  pop 
	    IL_005f:  ldloc.0 
	    IL_0060:  ldloc.2 
	    IL_0061:  ldloc.3 
	    IL_0062:  callvirt instance class [mscorlib]System.Security.Cryptography.ICryptoTransform class [mscorlib]System.Security.Cryptography.SymmetricAlgorithm::CreateDecryptor(unsigned int8[], unsigned int8[])
	    IL_0067:  stloc.s 4
	    .try { // 1
	      IL_0069:  ldloc.1 
	      IL_006a:  ldloc.s 4
	      IL_006c:  ldc.i4.0 
	      IL_006d:  newobj instance void class [mscorlib]System.Security.Cryptography.CryptoStream::'.ctor'(class [mscorlib]System.IO.Stream, class [mscorlib]System.Security.Cryptography.ICryptoTransform, valuetype [mscorlib]System.Security.Cryptography.CryptoStreamMode)
	      IL_0072:  stloc.s 5
	      .try { // 0
	        IL_0074:  ldloc.1 
	        IL_0075:  callvirt instance int64 class [mscorlib]System.IO.Stream::get_Length()
	        IL_007a:  ldloc.1 
	        IL_007b:  callvirt instance int64 class [mscorlib]System.IO.Stream::get_Position()
	        IL_0080:  sub 
	        IL_0081:  conv.ovf.i 
	        IL_0082:  newarr [mscorlib]System.Byte
	        IL_0087:  stloc.s 6
	        IL_0089:  ldloc.s 5
	        IL_008b:  ldloc.s 6
	        IL_008d:  ldc.i4.0 
	        IL_008e:  ldloc.s 6
	        IL_0090:  ldlen 
	        IL_0091:  conv.i4 
	        IL_0092:  callvirt instance int32 class [mscorlib]System.IO.Stream::Read(unsigned int8[], int32, int32)
	        IL_0097:  pop 
	        IL_0098:  ldloc.s 6
	        IL_009a:  stloc.s 7
	        IL_009c:  leave.s IL_00ca

	      } // end .try 0
	      finally  { // 0
	        IL_009e:  ldloc.s 5
	        IL_00a0:  brfalse.s IL_00a9

	        IL_00a2:  ldloc.s 5
	        IL_00a4:  callvirt instance void class [mscorlib]System.IDisposable::Dispose()
	        IL_00a9:  endfinally 
	      } // end handler 0
	    } // end .try 1
	    finally  { // 1
	      IL_00aa:  ldloc.s 4
	      IL_00ac:  brfalse.s IL_00b5

	      IL_00ae:  ldloc.s 4
	      IL_00b0:  callvirt instance void class [mscorlib]System.IDisposable::Dispose()
	      IL_00b5:  endfinally 
	    } // end handler 1
	  } // end .try 2
	  finally  { // 2
	    IL_00b6:  ldloc.1 
	    IL_00b7:  brfalse.s IL_00bf

	    IL_00b9:  ldloc.1 
	    IL_00ba:  callvirt instance void class [mscorlib]System.IDisposable::Dispose()
	    IL_00bf:  endfinally 
	  } // end handler 2
	} // end .try 3
	finally  { // 3
	  IL_00c0:  ldloc.0 
	  IL_00c1:  brfalse.s IL_00c9

	  IL_00c3:  ldloc.0 
	  IL_00c4:  callvirt instance void class [mscorlib]System.IDisposable::Dispose()
	  IL_00c9:  endfinally 
	} // end handler 3
	IL_00ca:  ldloc.s 7
	IL_00cc:  ret 
    } // end of method 7::2

    // method line 21
    .method public static hidebysig 
           default unsigned int8[] '3' (class [mscorlib]System.IO.Stream '0')  cil managed 
    {
        // Method begins at RVA 0x23d0
	// Code size 32 (0x20)
	.maxstack 4
	.locals init (
		unsigned int8[]	V_0)
	IL_0000:  ldarg.0 
	IL_0001:  callvirt instance int64 class [mscorlib]System.IO.Stream::get_Length()
	IL_0006:  conv.ovf.i 
	IL_0007:  newarr [mscorlib]System.Byte
	IL_000c:  stloc.0 
	IL_000d:  ldarg.0 
	IL_000e:  ldloc.0 
	IL_000f:  ldc.i4.0 
	IL_0010:  ldloc.0 
	IL_0011:  ldlen 
	IL_0012:  conv.i4 
	IL_0013:  callvirt instance int32 class [mscorlib]System.IO.Stream::Read(unsigned int8[], int32, int32)
	IL_0018:  pop 
	IL_0019:  ldloc.0 
	IL_001a:  call unsigned int8[] class '7'::'2'(unsigned int8[])
	IL_001f:  ret 
    } // end of method 7::3

  } // end of class 7

