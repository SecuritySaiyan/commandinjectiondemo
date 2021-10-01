package main

import (
	"crypto/cipher"
	"crypto/des"
	"crypto/md5"
	"crypto/rand"
	"crypto/rc4"
	"crypto/sha1"
	"encoding/hex"
	"fmt"
	"io"
	"net/http"
	"net/http/cgi"
	"os"
)

func main1() {
	// ruleid: insecure-module-used
	cgi.Serve(http.FileServer(http.Dir("/usr/share/doc")))
}

func main2() {
	// ruleid: insecure-module-used
	block, err := des.NewCipher([]byte("sekritz"))
	if err != nil {
		panic(err)
	}
	plaintext := []byte("I CAN HAZ SEKRIT MSG PLZ")
	ciphertext := make([]byte, des.BlockSize+len(plaintext))
	iv := ciphertext[:des.BlockSize]
	if _, err := io.ReadFull(rand.Reader, iv); err != nil {
		panic(err)
	}
	stream := cipher.NewCFBEncrypter(block, iv)
	stream.XORKeyStream(ciphertext[des.BlockSize:], plaintext)
	fmt.Println("Secret message is: %s", hex.EncodeToString(ciphertext))
}

func main3() {
	for _, arg := range os.Args {
		// ruleid: insecure-module-used
		fmt.Printf("%x - %s\n", md5.Sum([]byte(arg)), arg)
	}
}

func main4() {
	// ruleid: insecure-module-used
	cipher, err := rc4.NewCipher([]byte("sekritz"))
	if err != nil {
		panic(err)
	}
	plaintext := []byte("I CAN HAZ SEKRIT MSG PLZ")
	ciphertext := make([]byte, len(plaintext))
	cipher.XORKeyStream(ciphertext, plaintext)
	fmt.Println("Secret message is: %s", hex.EncodeToString(ciphertext))
}

func main5() {
	for _, arg := range os.Args {
		// ruleid: insecure-module-used
		fmt.Printf("%x - %s\n", sha1.Sum([]byte(arg)), arg)
	}
}

compute = input('\nYour expression? => ')
if not compute:
print ("No input")
else:
print ("Result =", eval(comp))

#lulzzz

api.token(eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9)


package main

import (
    "crypto/des"
    "crypto/md5"
    "crypto/rc4"
    "crypto/sha1"
    "fmt"
    "io"
    "log"
    "os"
)

func main() {
}

func test_des() {
    // NewTripleDESCipher can also be used when EDE2 is required by
    // duplicating the first 8 bytes of the 16-byte key.
    ede2Key := []byte("example key 1234")

    var tripleDESKey []byte
    tripleDESKey = append(tripleDESKey, ede2Key[:16]...)
    tripleDESKey = append(tripleDESKey, ede2Key[:8]...)
    // ruleid: use-of-DES
    _, err := des.NewTripleDESCipher(tripleDESKey)
    if err != nil {
        panic(err)
    }

    // See crypto/cipher for how to use a cipher.Block for encryption and
    // decryption.
}

func test_md5() {
    f, err := os.Open("file.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()

    defer func() {
        err := f.Close()
        if err != nil {
            log.Printf("error closing the file: %s", err)
        }
    }()

    // ruleid: use-of-md5
    h := md5.New()
    if _, err := io.Copy(h, f); err != nil {
        log.Fatal(err)
    }
    // ruleid: use-of-md5
    fmt.Printf("%x", md5.Sum(nil))
}

func test_rc4() {
    key := []byte{1, 2, 3, 4, 5, 6, 7}
    // ruleid: use-of-rc4
    c, err := rc4.NewCipher(key)
    dst := make([]byte, len(src))
    c.XORKeyStream(dst, src)
}

func test_sha1() {
    f, err := os.Open("file.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()
    // ruleid: use-of-sha1
    h := sha1.New()
    if _, err := io.Copy(h, f); err != nil {
        log.Fatal(err)
    }
    // ruleid: use-of-sha1
    fmt.Printf("%x", sha1.Sum(nil))
}
